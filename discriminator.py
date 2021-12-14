import torch
import torch.nn as nn
import torch.nn.functional as F

class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        
        self.conv1 = nn.Conv2d(1, 64, 7, 1, 3, padding_mode='reflect')
        self.bn1 = nn.BatchNorm2d(64)
        self.relu1 = nn.LeakyReLU()
        
        self.conv2 = nn.Conv2d(64, 128, 3, 2, 1, padding_mode='reflect')
        self.bn2 = nn.BatchNorm2d(128)
        self.relu2 = nn.LeakyReLU()
        
        self.conv2_1 = nn.Conv2d(128, 128, 3, 1, 1, padding_mode='reflect')
        self.bn2_1 = nn.BatchNorm2d(128)
        self.relu2_1 = nn.LeakyReLU()
        
        self.conv3 = nn.Conv2d(128, 256, 3, 2, 1, padding_mode='reflect')
        self.bn3 = nn.BatchNorm2d(256)
        self.relu3 = nn.LeakyReLU()
        
        self.conv3_1 = nn.Conv2d(256, 256, 3, 1, 1, padding_mode='reflect')
        self.bn3_1 = nn.BatchNorm2d(256)
        self.relu3_1 = nn.LeakyReLU()
        
        self.conv4 = nn.Conv2d(256, 512, 3, 2, 1, padding_mode='reflect')
        self.bn4 = nn.BatchNorm2d(512)
        self.relu4 = nn.LeakyReLU()
        
        self.conv4_1 = nn.Conv2d(512, 512, 3, 1, 1, padding_mode='reflect')
        self.bn4_1 = nn.BatchNorm2d(512)
        self.relu4_1 = nn.LeakyReLU()
        
        self.conv5 = nn.Conv2d(512, 1024, 3, 1, 1, padding_mode='reflect')
        self.bn5 = nn.BatchNorm2d(1024)
        self.relu5 = nn.LeakyReLU()
        
        self.conv5_1 = nn.Conv2d(1024, 1, 3, 1, 1, padding_mode='reflect')
        
        
    def forward(self, x):
        
        x = self.relu1(self.bn1(self.conv1(x)))
        x = self.relu2(self.bn2(self.conv2(x)))
        x = self.relu2_1(self.bn2_1(self.conv2_1(x)))
        x = self.relu3(self.bn3(self.conv3(x)))
        x = self.relu3_1(self.bn3_1(self.conv3_1(x)))
        x = self.relu4(self.bn4(self.conv4(x)))
        x = self.relu4_1(self.bn4_1(self.conv4_1(x)))
        x = self.relu5(self.bn5(self.conv5(x)))
        x = self.conv5_1(x)
        
        return x