import torch
import psutil
from multiprocessing import Process
import time

import watcher
import os

def print_ram(pidid):
    while(1):
        print(u'当前进程的内存使用：%.4f GB' % (psutil.Process(pidid).memory_info().rss / 1024 / 1024 / 1024) )
        time.sleep(0.1)

nowpid =os.getpid()
# p = Process(target=print_ram, args=(nowpid,))
# print(nowpid)
# p.start()

w = watcher.Watcher(nowpid)
w.Start()
model = torch.hub.load('pytorch/vision:v0.6.0', 'mobilenet_v2', pretrained=True)
model.eval()

from PIL import Image
from torchvision import transforms
input_image = Image.open("dog.jpg")
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
input_tensor = preprocess(input_image)
input_batch = input_tensor.unsqueeze(0) # create a mini-batch as expected by the model

# move the input and model to GPU for speed if available
# if torch.cuda.is_available():
#     input_batch = input_batch.to('cuda')
#     model.to('cuda')
while(1):

    with torch.no_grad():
        output = model(input_batch)
time.sleep(0.1)
# Tensor of shape 1000, with confidence scores over Imagenet's 1000 classes
print(output[0])
# The output has unnormalized scores. To get probabilities, you can run a softmax on it.
print(torch.nn.functional.softmax(output[0], dim=0))
# 
