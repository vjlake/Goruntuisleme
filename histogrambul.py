#!/usr/bin/env python
# coding: utf-8

# In[3]:


def histogrambul(grimatris):
    hist=[0 for c in range(256)]
    for we in grimatris:
        for te in we:
            hist[te]=hist[te]+1
    return hist

