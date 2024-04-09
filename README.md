# Making a GPT (Generative Pretrained Transformer)
> In this project we'll basically try to model a character sequence of words. This work was mostly if not full inspired by the following publication [website](https://arxiv.org/pdf/1706.03762.pdf)

> It's most convenient if the following program is run using a GPU via conda Pytorch

## Installing and setting up Anaconda
Using wget:
```bash
wget https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh
chmod +x Anaconda3-2021.11-Linux-x86_64.sh
./Anaconda3-2021.11-Linux-x86_64.sh
```

Using curl:
```bash
curl -O https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh
chmod +x Anaconda3-2021.11-Linux-x86_64.sh
./Anaconda3-2021.11-Linux-x86_64.sh
```

Verify installation:
```bash
conda --version
```

Update Conda
```bash
conda update -n base -c defaults conda
```

## Creating a PyTorch virtual environment using Anaconda
1. **Create a New Environment**: Use the conda create command to create a new virtual environment. You can specify the Python version and any additional packages you need. For PyTorch, you can also specify the version of PyTorch you want to install. For example:

```bash
conda create -n myenv python=3.8
```
2. **Activate the Environment**: Once the environment is created, activate it using:

```bash
conda activate myenv 
```

> Note: You can delete a virtual environment with the following command:
```bash 
conda env list                      # Lists all the env(s) 
conda remove --name ENV_NAME --all  # Removes the select env
```

3. **Install PyTorch**: Once the environment is activated, you can install PyTorch using the conda install command. You should specify the appropriate version of PyTorch depending on your requirements. For example, to install PyTorch with CUDA support for GPU acceleration:

```bash
conda install pytorch torchvision torchaudio cudatoolkit -c pytorch 
```
4. **Verifying Cuda is working:** After all that installations you need to cross-check whether CUDA is available. CUDA is a parallel computing platform and application programming interface (API) model created by Nvidia. In order for torch.cuda.is_available() to return True, you need to meet the following requirements:

   1. *Nvidia GPU:* You need to have a Nvidia GPU installed on your system.
   2. *CUDA Toolkit:* You need to have the CUDA Toolkit installed on your system. This includes CUDA drivers and the CUDA runtime library.
   3. *PyTorch with CUDA support:* You need to have PyTorch installed with CUDA support. You can typically install the appropriate version of PyTorch using pip or conda, ensuring it matches the CUDA version installed on your system.

    > Here's a basic outline of the steps you might take to ensure torch.cuda.is_available() returns <span style=" color: green">True</span>:

    1. *Check your GPU:* Ensure you have an Nvidia GPU installed on your system.
    2. *Install CUDA Toolkit:* Download and install the CUDA Toolkit from Nvidia's website. Make sure to follow the installation instructions carefully.
    3. *Install PyTorch with CUDA support:* Install PyTorch with CUDA support. If you're using pip, you might use a command like:  