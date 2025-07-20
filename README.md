
# Wall Crack Detection - CycleGAN 🌀✨

A PyTorch-based CycleGAN model that transforms blurred images into clear images using unpaired image-to-image translation. Trained using the official [pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) framework.

---

## 📁 Dataset Structure

The dataset follows the unaligned CycleGAN format:

```

datasets/
└── blur2clear/
├── trainA/      # Blurred images (Domain A)
├── trainB/      # Clear images (Domain B)
├── testA/       # Blurred test images
└── testB/       # (Optional) Clear test images

````

💡 Only the first 500 images were used for initial training to accelerate experimentation.

---

## 🚀 Training

To train the CycleGAN model:

```bash
python train.py \
  --dataroot "A:/MACHINE LEARNING/datasets/blur2clear" \
  --name blur2clear_cyclegan \
  --model cycle_gan \
  --n_epochs 10 \
  --n_epochs_decay 5 \
  --gpu_ids 0 \
  --load_size 128 \
  --crop_size 128
````

* `n_epochs`: Number of epochs with initial learning rate.
* `n_epochs_decay`: Linear decay after `n_epochs`.

> ✅ Training checkpoints and logs are saved to `checkpoints/blur2clear_cyclegan/`.

---

## 🧪 Testing

To test on new images:

```bash
python test.py \
  --dataroot "A:/MACHINE LEARNING/datasets/blur2clear" \
  --name blur2clear_cyclegan \
  --model cycle_gan \
  --gpu_ids 0 \
  --load_size 128 \
  --crop_size 128
```

🔍 Results will be saved to:

```
results/blur2clear_cyclegan/test_latest/images/
```

---

## 🖼️ Visual Results

After training, visual output is viewable at:

```
checkpoints/blur2clear_cyclegan/web/index.html
```

It includes side-by-side comparisons of:

* Real A (blurred input)
* Fake B (generated clear)
* Real B (ground truth clear, if available)
* Reconstructed A (cycle consistency)

---

## 🧠 Model Architecture

CycleGAN uses two generators and two discriminators:

* G<sub>A→B</sub>: Blurred → Clear
* G<sub>B→A</sub>: Clear → Blurred
* D<sub>A</sub>, D<sub>B</sub>: PatchGAN discriminators

---

## 💻 System Info

* 💻 Trained on: Local machine (Windows)
* 🧠 Framework: PyTorch
* 🎞️ Dataset: 20k blurred and clear images (subset of 500 used initially)
* 🐍 Python: 3.10

---

## 📌 Future Work

* Train on full 20k dataset
* Improve deblurring quality with deeper GANs or attention
* Export trained model for inference in apps (ONNX/TorchScript)
* Integrate with UI (Flutter or Tkinter)

---

## 🧑‍💻 Author

**Sreehari** — [R3CTR](https://github.com/Sree14hari)
Passionate about AI, ML, and building impactful tools.

---
