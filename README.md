
# Wall Crack Detection - CycleGAN 🏗️🌀

[![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?logo=PyTorch&logoColor=white)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A PyTorch implementation for enhancing wall crack detection images using CycleGAN, based on the [pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) framework.

## Project Structure 📂

```
pytorch-CycleGAN-and-pix2pix/
├── WALL_CRACK/
│   ├── blur_ds/
│   │   ├── trainA/       # Blurred wall images
│   │   └── trainB/       # Clear wall images
│   ├── MiniBlur/         # Subset for quick testing
│   │   ├── trainA/
│   │   └── trainB/
│   └── shadow_ds/        # Shadow augmentation dataset
│       ├── trainA/
│       └── trainB/
├── scripts/
│   ├── blur_add.py       # Add blur to images
│   ├── ds_download.py    # Dataset download utility
│   ├── shadow_add.py     # Add shadows to images
│   └── subsetblur.py     # Create subset datasets
├── cuda_test.py          # CUDA availability test
└── README.md
```

## Datasets 🌉

### Main Datasets:
1. **blur_ds** - Primary dataset for blur-to-clear transformation
   - `trainA/`: Clear wall crack images
   - `trainB/`: Corresponding Blured clear images

2. **shadow_ds** - For shadow augmentation training
   - `trainA/`: Clean images
   - `trainB/`: Shadowed versions

3. **MiniBlur** - Subset for rapid prototyping
   - Contains 500 samples from blur_ds

## Scripts 🛠️

### Data Preparation:
- `blur_add.py`: Add synthetic blur to images
- `shadow_add.py`: Add shadow effects to images
- `subsetblur.py`: Create smaller dataset subsets
- `ds_download.py`: Download dataset from external sources

### Utility:
- `cuda_test.py`: Verify CUDA availability and GPU compatibility

## Quick Start 🚀

1. **Prepare Datasets**:
```bash
python scripts/subsetblur.py --source blur_ds --target MiniBlur --size 500
```

2. **Add Augmentations**:
```bash
python scripts/blur_add.py --input_dir datasets/clear --output_dir blur_ds/trainA
python scripts/shadow_add.py --input_dir datasets/clear --output_dir shadow_ds/trainA
```

3. **Verify Environment**:
```bash
python cuda_test.py
```

4. **Train Model**:
```bash
python train.py --dataroot ./WALL_CRACK/blur_ds --name wallcrack_cyclegan --model cycle_gan
```

## Training Options ⚙️

```bash
python train.py \
  --dataroot ./WALL_CRACK/blur_ds \
  --name wallcrack_model \
  --model cycle_gan \
  --batch_size 4 \
  --n_epochs 50 \
  --n_epochs_decay 50 \
  --save_epoch_freq 10 \
  --display_freq 100
```

## Results Visualization 🌟

View training progress:
```bash
python -m visdom.server
```
Then open `http://localhost:8097` in your browser.

## License 📄

MIT License - See [LICENSE](LICENSE) for details.

---
**Maintainer**: Sreehari ([@Sree14hari](https://github.com/Sree14hari))  
**Contact**: sreehari14shr@gmail.com
**Organization**: R3ACTR
```
