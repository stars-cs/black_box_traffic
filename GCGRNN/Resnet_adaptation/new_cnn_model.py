import torch
import torch.nn as nn

"""
The Residual block:
    - Contains 3 Convolutions, each followed by a  BatchNorm
    - Each residual block increases the dimensionality by 4 times (i.e. expansion =4, used in Conv3 and BN3)

    Identity downsample = to match the size of skip connection and the current operandi
    In case we change the input size or the number of channels somewhere
"""
class block(nn.Module):
    def __init__(self, in_channels, out_channels, identity_downsample = None, stride = 1):

        super(block, self).__init__()
        self.expansion = 4
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size = 1, stride = 1, padding = 0 )
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size = 3, stride = stride, padding = 1)
        self.bn2 = nn.BatchNorm2d(out_channels)
        self.conv3 = nn.Conv2d(out_channels, out_channels* self.expansion, kernel_size = 1, stride = 1, padding = 0)
        self.bn3 = nn.BatchNorm2d(out_channels*self.expansion)
        self.relu = nn.ReLU()
        self.identity_downsample = identity_downsample

    def forward(self,x):
        identity = x
        #print("\nBefore 1 : ", x.shape)
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        #print("Before 2 : ", x.shape)
        x = self.conv2(x)
        x = self.bn2(x)
        x = self.relu(x)
        #print("Before 3 : ", x.shape)
        x = self.conv3(x)
        x = self.bn3(x)
        x = self.relu(x)

        if self.identity_downsample is not None:
            identity = self.identity_downsample(identity)

        # add a skip connection to the current version of x
        x += identity
        x = self.relu(x)

        return x
"""
The ResNet50 model Adaptation:
    - Does not contain MaxPool
"""

class ResNet_Adaptation(nn.Module):
    def __init__(self, block, layers, channels, output_size):
        # block is the ResNet block class that was defined above
        # layers = In each resnet layer, how many times we want to use the block
        # In the resnet 50, layers = [3,4,6,3] in the first resnet layer, use the block 3 times...
        # For a univariate time series, channels = 1
        super(ResNet_Adaptation, self).__init__()

        # what are these in_channels?
        # take 1 input and generate 64 feature maps
        self.in_channels = 64
        self.conv1 = nn.Conv2d(channels, 64 , kernel_size = 8, stride =1 , padding = 1 )
        self.bn1 = nn.BatchNorm2d(64)
        self.relu = nn.ReLU()

        self.dropout1 = nn.Dropout(0.01)
        self.dropout2 = nn.Dropout(0.01)

        self.layer1 = self._make_layer(block, layers[0], out_channels = 64, stride = 1)
        self.layer2 = self._make_layer(block, layers[1], out_channels = 64, stride = 2)
        self.layer3 = self._make_layer(block, layers[2], out_channels = 128, stride = 2)

        #self.layer3 = self._make_layer(block, layers[2], out_channels = 256, stride = 2)
        #self.layer4 = self._make_layer(block, layers[3], out_channels = 512, stride = 2)

        # For 1d, this only has 1 output
        # Average pooling of signal over different planes
        self.avgpool = nn.AdaptiveAvgPool2d((1,1))

        # 512 = number of feature maps, 4 = expansion from each block
        self.fc1 = nn.Linear(128*4, 1024)
        self.fc2 = nn.Linear(1024, output_size)
        #self.fc = nn.Linear(512*4, output_size)

    # Now ResNet
    # This function makes the list of layers
    def _make_layer(self, block, num_residual_blocks, out_channels, stride):
        # block is the ResNet block class that was defined above
        # num_residual_blocks gives number of times block will be used
        # out_channels = number of channels we want after we are done with what??
        identity_downsample = None
        layers = []

        # When the stride is 1, the size of the identity and the conv output is the same and we have no problem adding
        # Why the second case? ( The length of each time series is fine but the number of feature maps are different)
        if stride != 1 or self.in_channels != out_channels*4:

            # This makes the addition possible
            # We want the same size input and the same number of feature maps
            identity_downsample = nn.Sequential(nn.Conv2d(self.in_channels, out_channels*4, kernel_size = 1, stride=stride),
                                                nn.BatchNorm2d(out_channels*4))

        #  This is tricky
        # Change the number of channels
        layers.append(block(self.in_channels, out_channels, identity_downsample, stride))

        # We defined abovem, for the first layer to have 64 activation maps
        # This will mumtiply it
        self.in_channels = out_channels*4 #256

        # -1 because we defined one layer above
        for i in range(num_residual_blocks -1):
            layers.append(block(self.in_channels, out_channels)) # in_channels = 256, out_channels = 64

        return nn.Sequential(*layers)

    def forward(self, x):
        # Add a channel dimension
        # Without the unsqueeze, it would not understand that the input is 1d

        # Maybe we dont need an unsqueeze for 2d
        x= x.unsqueeze(1)

        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.dropout1(x)
        # Are these the blocks?
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        #x = self.layer4(x)

        x = self.avgpool(x)

        # View / flatten before FC
        #print("shape before flatten", x.shape)
        x = x.reshape(x.shape[0],-1)
        x = self.dropout2(x)
        x = self.fc1(x)
        x = self.fc2(x)

        return x

def ResNet_Adaptation_model(channels = 1, output_size = 1800):
    #return ResNet_Adaptation(block, [3,4,6,3], channels, output_size)
    return ResNet_Adaptation(block, [3,4,3], channels, output_size)

# Actually this value [3,4,6,3] is for ResNet50. Need to find our own for this adaptation
