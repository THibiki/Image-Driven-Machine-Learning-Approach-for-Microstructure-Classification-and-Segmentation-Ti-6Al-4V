"""
----------------------------------ABOUT-----------------------------------
Author: Arun Baskaran
--------------------------------------------------------------------------
"""

# Testing edits

import lib_imports
from aux_funcs import *
import model_params
import sys
from pathlib import Path

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: main <mode>", file=sys.stderr)
        sys.exit(-1)
    mode = sys.argv[1] 
    train_images, train_labels, test_images, test_labels, validation_images, validation_labels, test_images_id = load_images_labels()
    
    if mode == "training" :
        model = train_model()
    
    elif mode =="load":
        model = load_model()
        
    test_accuracy(model, test_images, test_labels)
    
    y_classes = get_predicted_classes(model, test_images)

    output_dir = Path(__file__).resolve().parent.parent / "outputs" / "segmentation"
    feature_segmentation(y_classes, test_images_id, output_dir)



