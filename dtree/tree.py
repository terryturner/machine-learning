#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'enginebai'

from math import log

def calculate_entropy(dataset):
    """
    計算一個數據的entropy。
    :param dataset:
    :return:
    """
    num_entries = len(dataset)
    # 為所有可能的分類建立dict方便做查詢
    label_count = {}
    for feature_vector in dataset:
        current_label = feature_vector[-1]
        if current_label not in label_count.keys():
            label_count[current_label] = 0
        label_count[current_label] += 1

    entropy = 0.0
    for label in label_count:
        prob = float(label_count[label]) / num_entries
        entropy -= prob * log(prob, 2)
    return entropy

def create_data_set():
    data_set = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    labels = ['no', 'flippers']
    return data_set, labels

def split_data_set(data_set, axis, value):
    """
    依照給定的特徵劃分資料集合。
    :param data_set: 待劃分的資料集合
    :param axis: 劃分資料集合的特徵值
    :param value: 需要回傳的特徵值
    :return:
    """
    new_data_set = []
    for feature_vector in data_set:
        if feature_vector[axis] == value:
            reduced_feature_vector = feature_vector[:axis]
            reduced_feature_vector.extend(feature_vector[axis + 1:])
            new_data_set.append(reduced_feature_vector)
    return new_data_set

def choose_best_feature_to_split(data_set):
    num_feature = len(data_set[0]) - 1
    base_entropy = calculate_entropy(data_set)
    best_info_gain = 0.0
    best_feature = -1
    for i in range(num_feature):
        feature_list = [instance[i] for instance in data_set]
        unique_value = set(feature_list)
        new_entropy = 0.0
        for value in unique_value:
            sub_data_set = split_data_set(data_set, i, value)
            prob = len(sub_data_set) / float(len(data_set))
            new_entropy += prob * calculate_entropy(sub_data_set)
        info_gain = base_entropy - new_entropy
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature = i

    return best_feature