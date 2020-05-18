#!/usr/bin/python
################################
# module: image_retrieval.py
# Brock Francom
# A02052161
#################################
import cv2
import sys
import os
import pickle
from matplotlib import pyplot as plt
from os.path import basename

def show_images(input_image, match_list):
  # show image 1
  inrgb = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)
  fig1 = plt.figure(1)
  fig1.suptitle('Input Image')
  plt.imshow(inrgb)

  # show matched image 1
  #print('match 1 ' + match_list[0][0])
  retimg1 = cv2.imread(match_list[0][0])
  simscore1 = match_list[0][1]
  retimg1= cv2.cvtColor(retimg1, cv2.COLOR_BGR2RGB)
  fig2 = plt.figure(2)
  fig2.suptitle('Matched Image 1: ' + basename(match_list[0][0]) + '; Sim = ' + str(simscore1))
  plt.imshow(retimg1)

  # show matched image 2
  #print('match 2 ' + match_list[1][0])
  retimg2 = cv2.imread(match_list[1][0])
  simscore2 = match_list[1][1]
  retimg2= cv2.cvtColor(retimg2, cv2.COLOR_BGR2RGB)
  fig3 = plt.figure(3)
  fig3.suptitle('Matched Image 2: ' + basename(match_list[1][0]) + '; Sim = ' + str(simscore2))
  plt.imshow(retimg2)

  # show matched image 3
  #print('match 3 ' + match_list[2][0])
  retimg3 = cv2.imread(match_list[2][0])
  simscore3 = match_list[2][1]
  retimg3= cv2.cvtColor(retimg3, cv2.COLOR_BGR2RGB)
  fig4 = plt.figure(4)
  fig4.suptitle('Matched Image 3: ' + basename(match_list[2][0]) + '; Sim = ' + str(simscore3))
  plt.imshow(retimg3)

  plt.show()

def find_sim_rgb_images(imgpath, num_bins, hist_index, hist_sim): 
    im = cv2.imread(imgpath)
    histcomp = cv2.calcHist(im, [0,1,2], None, [num_bins,num_bins,num_bins], [0,256, 0,256, 0,256])
    cv2.normalize(histcomp,histcomp).flatten()

    if hist_sim == 'bhatta':
        #0 means same, 1 means different
        top_matches = []
        best = 1
        for hist in hist_index.keys():
            sim_score = cv2.compareHist(histcomp, hist_index[hist], cv2.HISTCMP_BHATTACHARYYA)
            if sim_score <= best:
                best = sim_score
                if len(top_matches) < 3:
                    top_matches.append((hist, sim_score))
                else:
                    top_matches.append((hist, sim_score))
                    top_matches.remove(top_matches[0])
        top_matches.reverse()
        return top_matches
    
    if hist_sim == 'correl':
        #1 means same, 0 means different
        top_matches = []
        best = 0
        for hist in hist_index.keys():
            sim_score = cv2.compareHist(histcomp, hist_index[hist], cv2.HISTCMP_CORREL)
            if sim_score >= best:
                best = sim_score
                if len(top_matches) < 3:
                    top_matches.append((hist, sim_score))
                else:
                    top_matches.append((hist, sim_score))
                    top_matches.remove(top_matches[0])
        return top_matches

    if hist_sim == 'inter':
        #low means different, high means same. 
        top_matches = []
        best = 0
        for hist in hist_index.keys():
            sim_score = cv2.compareHist(histcomp, hist_index[hist], cv2.HISTCMP_INTERSECT)
            if sim_score >= best:
                best = sim_score
                if len(top_matches) < 3:
                    top_matches.append((hist, sim_score))
                else:
                    top_matches.append((hist, sim_score))
                    top_matches.remove(top_matches[0])
        return top_matches
        
    if hist_sim == 'chisqr':
        #0 means same, big means different
        top_matches = []
        best = 9999999999
        for hist in hist_index.keys():
            sim_score = cv2.compareHist(histcomp, hist_index[hist], cv2.HISTCMP_CHISQR)
            if sim_score <= best:
                best = sim_score
                if len(top_matches) < 3:
                    top_matches.append((hist, sim_score))
                else:
                    top_matches.append((hist, sim_score))
                    top_matches.remove(top_matches[0])
        return top_matches

def find_sim_hsv_images(imgpath, num_bins, hist_index, hist_sim):  
    im = cv2.imread(imgpath)
    histcomp = cv2.calcHist(im, [0,1,2], None, [num_bins,num_bins,num_bins], [0,180, 0,256, 0,256])
    cv2.normalize(histcomp,histcomp).flatten()

    if hist_sim == 'bhatta':
        #0 means same, 1 means different
        top_matches = []
        best = 1
        for hist in hist_index.keys():
            sim_score = cv2.compareHist(histcomp, hist_index[hist], cv2.HISTCMP_BHATTACHARYYA)
            if sim_score <= best:
                best = sim_score
                if len(top_matches) < 3:
                    top_matches.append((hist, sim_score))
                else:
                    top_matches.append((hist, sim_score))
                    top_matches.remove(top_matches[0])
        top_matches.reverse()
        return top_matches
    
    if hist_sim == 'correl':
        #1 means same, 0 means different
        top_matches = []
        best = 0
        for hist in hist_index.keys():
            sim_score = cv2.compareHist(histcomp, hist_index[hist], cv2.HISTCMP_CORREL)
            if sim_score >= best:
                best = sim_score
                if len(top_matches) < 3:
                    top_matches.append((hist, sim_score))
                else:
                    top_matches.append((hist, sim_score))
                    top_matches.remove(top_matches[0])
        return top_matches

    if hist_sim == 'inter':
        #low means different, high means same. 
        top_matches = []
        best = 0
        for hist in hist_index.keys():
            sim_score = cv2.compareHist(histcomp, hist_index[hist], cv2.HISTCMP_INTERSECT)
            if sim_score >= best:
                best = sim_score
                if len(top_matches) < 3:
                    top_matches.append((hist, sim_score))
                else:
                    top_matches.append((hist, sim_score))
                    top_matches.remove(top_matches[0])
        return top_matches
        
    if hist_sim == 'chisqr':
        #0 means same, big means different
        top_matches = []
        best = 9999999999
        for hist in hist_index.keys():
            sim_score = cv2.compareHist(histcomp, hist_index[hist], cv2.HISTCMP_CHISQR)
            if sim_score <= best:
                best = sim_score
                if len(top_matches) < 3:
                    top_matches.append((hist, sim_score))
                else:
                    top_matches.append((hist, sim_score))
                    top_matches.remove(top_matches[0])
        return top_matches

def load_hinx(pick_path):
  with open(pick_path, 'rb') as histfile:
    return pickle.load(histfile)



