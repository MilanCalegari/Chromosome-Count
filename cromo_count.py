# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 22:46:03 2019

@author: Rodrigo Calegari
"""

from matplotlib import pyplot as plt
from skimage.feature import blob_dog, blob_log, blob_doh
from math import sqrt
import glob
from skimage.io import imread

def count_cromo():
  #importing the image and converting to gray
  imagem = input('Input the image (jpg, gif...) : ')
  exemple = glob.glob(imagem)[0]
  im = imread(exemple, as_gray=True)
  print('ongoing process...')

  #analyzing the image
  blobs_log = blob_log(im, max_sigma=42, num_sigma=20, min_sigma=14, threshold=.0001, overlap=0 )
  blobs_log[:,2] = blobs_log[:,2] * sqrt(2)
  numrows = len(blobs_log)
  print(str(imagem)  + ' have abot ' + str(numrows) + ' chromosomes')
  print('\nChromosomes find: ')

  #generating the output
  fig, ax = plt.subplots(1,1)
  plt.imshow(im, cmap='gray')
  for blob in blobs_log:
    y,x,r = blob
    c = plt.Circle((x,y), r+5, color='lime', linewidth=2, fill=False)
    ax.add_patch(c)
  plt.show()
  
  
saida = 1

while saida != '0':
    count_cromo()
    saida = input('''For continue type 1.
For exit type 0 : ''')
