import backbone
import utils

import torch
import torch.nn as nn
from torch.autograd import Variable
import numpy as np
import torch.nn.functional as F

class BaselineTrain(nn.Module):
    def __init__(self, model_func, num_class,loss_type):
        super(BaselineTrain, self).__init__()
        self.feature    = model_func()

        self.classifier = backbone.distLinear(self.feature.final_feat_dim, num_class)
        self.loss_type = loss_type  
        self.num_class = num_class
        self.loss_fn = nn.CrossEntropyLoss()

    def forward(self,x,y):
        x    = Variable(x.cuda())
        out  = self.feature.forward(x)
        scores  = self.classifier.forward(out,y)
        return scores

    def forward_loss(self, x, y):
        scores = self.forward(x,y)
        y = Variable(y.cuda())
        return self.loss_fn(scores, y )
    
    def train_loop(self, epoch, train_loader, optimizer):
        print_freq = 10
        avg_loss=0

        for i, (x,y) in enumerate(train_loader):
            optimizer.zero_grad()
            loss = self.forward_loss(x, y)
            loss.backward()
            optimizer.step()

            avg_loss = avg_loss+loss.item()

            if i % print_freq==0:
                #print(optimizer.state_dict()['param_groups'][0]['lr'])
                print('Epoch {:d} | Batch {:d}/{:d} | Loss {:f}'.format(epoch, i, len(train_loader), avg_loss/float(i+1)  ))
                     
    def test_loop(self, val_loader):
        return -1 #no validation, just save model during iteration

