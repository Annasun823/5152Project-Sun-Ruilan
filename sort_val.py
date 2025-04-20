import os
import shutil

# Make sure this is your ImageNet `val/` directory.
val_dir = r"C:\Users\Sun Ruilan\examples\imagenet\val"
devkit_dir = r"C:\Users\Sun Ruilan\examples\imagenet\ILSVRC2012_devkit_t12\data"

# Read ImageNet category mapping file
label_file = os.path.join(devkit_dir, "ILSVRC2012_validation_ground_truth.txt")
map_file = os.path.join(devkit_dir, "map_clsloc.txt")

# Read Category ID Mapping
with open(map_file, "r") as f:
    wnid_map = {str(i + 1): line.split()[0] for i, line in enumerate(f.readlines())}

# Read the true category of the validation set image
with open(label_file, "r") as f:
    labels = f.read().splitlines()

# Processing each image
for i, label in enumerate(labels):
    wnid = wnid_map[label]  # Get the category name, e.g. ‘n01440764’
    class_dir = os.path.join(val_dir, wnid)
    os.makedirs(class_dir, exist_ok=True)

    # Move images to the corresponding category folder
    img_name = f"ILSVRC2012_val_{i+1:08d}.JPEG"
    src_path = os.path.join(val_dir, img_name)
    dst_path = os.path.join(class_dir, img_name)

    if os.path.exists(src_path):
        shutil.move(src_path, dst_path)
        print(f"MOVE {img_name} TO {class_dir}/")

print("`val/` Catalogue classification completed! ")
