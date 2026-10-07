# Changelog

## 2026-10-07 — Python 3.12 compatibility and pipeline fixes

### Environment

- Used Python 3.12.3 virtual environment
- Used imports with TensorFlow 2.21.0, Keras 3.15.1, NumPy 2.5.3 and segmentation-models 1.0.1
- The segmentation library remains a legacy dependency to keep the notebook existing ResNet34 U-Net implementation

### Classification and feature segmentation (`src`)

- Replaced `tensorflow.python.keras` imports with `tensorflow.keras` imports
- Imported watershed from `skimage.segmentation` and updated its call site
- Added `sys` import in `main.py`
- Added library for parameter imports in `aux_funcs.py`
- Replaced the removed `tf.contrib` initializer with `glorot_uniform`
- Used the Keras `zeros` initializer for biases
- Converted spreadsheet labels to a NumPy integer array before subtracting one, avoiding mutation of a pandas Series through indexed assignments
- Added `image_path()` to select `Images1` and `Images2`
- Replaced backend encoding with `keras.utils.to_categorical()`
- Loaded the original `weights/classification.ckpt` using `tf.train.load_checkpoint()`
- Used `pathlib.Path` to create and save PNGs under project-root `outputs/segmentation` with the directory passed from `main.py`

### Few-shot notebook (`Semantic Segmentation/few_shot_ti64.ipynb`)

- Disabled the in-notebook pip installation cell and dependencies are installed in the active environment beforehand
- Selected `SM_FRAMEWORK=tf.keras` and `KERAS_BACKEND=tensorflow` before imports
- Updated watershed imports calls for integer marker arrays and figure closing
- Defined the shared network image size as 256 the lamellar mask-generation helper retains its original local size of 604
- Used nearest neighbor resizing and a fixed threshold for binary reference masks
- Retained foreground class 1 for lamellar masks and class 2 for equiaxed masks
- Removed the unsupported `dtype` argument from `to_categorical()` and converted the resulting arrays to float32
- Fixed the undefined `num` reference in the equiaxed mask-generation loop
- Extended both mask-generation loops to images, covering training and test images 
- Existing masks are preserved and missing masks are saved with write failure checks
- Applied the same preprocessing during training and prediction, using prediction batches of one image
- Replaced the evaluation block containing the undefined `test_dup_mask_paths`
- Evaluation now compares argmax class labels, computes pixel accuracy and uses the appropriate foreground class for per-image IoU
- Images with zero foreground union are excluded from the mean foreground IoU
- Retained ImageNet-initialized ResNet34 U-Net, a training batch size of 3, fixed 5 epochs and 20 test images. Early stopping was not added
