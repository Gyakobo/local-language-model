import torch
import torch.nn as nn
from torch.nn import functional as F

n_embd = 32
block_size = 8
device = 'cude' if torch.cuda.is_available() else 'cpu'

torch.manual_seed(1337)
