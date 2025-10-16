# ollama-setup

This manual shows steps to be used for setting up OLLAMA on a windows laptop with NVIDIA GPU.

# Prerequisites
1. Windows 10 or 11
2. Internet connection
3. NVIDIA GPU with CUDA support (recommended)
4. SSD drive for better performance (recommended)
5. At least 16GB RAM (32GB or more recommended for better performance)
6. At least 10GB of free disk space
7. Administrative access to the laptop
8. Basic knowledge of command line operations


# Setup Steps
## Step 1: Install NVIDIA Drivers, if you have Nvidia GPU
1. Go to the [NVIDIA Driver Download page](https://www.nvidia.com/Download/index.aspx).
2. Select your GPU model and operating system, then click "Search". 
3. Download and install the latest drivers. Follow the on-screen instructions to complete the installation.
4. Restart your computer if prompted.

## Step 2: Install CUDA Toolkit, if you have Nvidia GPU
1. Go to the [CUDA Toolkit Download page](https://developer.nvidia.com/cuda-downloads).
2. Select your operating system, architecture, and version, then click "Download".
3. Run the installer and follow the on-screen instructions to complete the installation.
4. Restart your computer if prompted.

## Step 3: Setup Environment Variables
1. Open the Start Menu and search for "Environment Variables".
2. Click on "Edit the system environment variables".
3. In the System Properties window, click on the "Environment Variables" button.
4. Under "System variables", find and set the `OLLAMA_MODELS` variable, with value specifying directory on SSD disk.
5. Click "OK" to save the changes and close all dialog boxes.
6. Set the following environment variables in the same way, if you have Nvidia GPU:
    - `CUDA_VISIBLE_DEVICES`: Set to the GPU IDs you want to use (e.g., "0,1" for first two GPUs).
        > You will find GPU IDs using `Task Manager` -> `Performance` tab -> `GPU` section.
    - `OLLAMA_GPU_MEMORY_FRACTION`: Set to a value between 0 and 1 to limit the fraction of GPU memory OLLAMA can use (e.g., "0.8" for 80%).


> Please note model will be downloaded to this directory, ensure it has sufficient space and is on SSD for better performance.


## Step 4: Download and Install OLLAMA on Windows
1. Go to the [OLLAMA official website](https://ollama.com/).
2. Download the latest version of OLLAMA for Windows.
3. Run below command in `cmd` or `powershell` prompt to install the downloaded file:
   ```
   ollamasetup.exe /Dir="Directory Path to install Ollama to"
   ```

# Identifying models
1. Browse available models on the [OLLAMA Models page](https://ollama.com/models).
2. Choose a model that fits your requirements and note its name for use in the next step
3. You might want to choose at minimum 2 models for generating embedding and another for generating NLP responses

# Running OLLAMA
1. Open `cmd` or `powershell` prompt.
2. Navigate to the OLLAMA installation directory:
   ```
   cd "Directory Path where Ollama is installed"
   ```
3. Run OLLAMA with the desired model:
   ```
    ollama run <model-name>
    ```
4. If model was not previously installed in location specified by `OLLAMA_MODELS`(Setup step), then it will be downloaded to that location

