from dataset_toolkit import Toolkit

dataset_dir = "/mnt/sda/DataLake/Seafile/daimler_bus_dataset_tf/images/"
old_annotation_dir = "/mnt/sda/DataLake/Seafile/daimler_bus_dataset_tf/test"
old_format = "xml"

new_save = "/mnt/sda/DataLake/Seafile/cleaned_daimler_bus"
new_format = "darknet"

Toolkit.convert(dataset_dir, old_annotation_dir, old_format,
               new_save, new_format)
