import tensorflow as tf
from load_3D_data import num_labels

def create_model(args, input_shape):
    # If using CPU or single GPU
    if args.gpus <= 1:
        if args.net == 'unet':
            from unet import UNet
            model = UNet(input_shape)
            return [model]
        elif args.net == 'segcapsr1':
            from capsnet import CapsNetR1
            model_list = CapsNetR1(input_shape)
            return model_list
        elif args.net == 'segcapsr3':
            from capsnet import CapsNetR3
            model_list = CapsNetR3(input_shape)
            return model_list
        elif args.net == 'capsbasic':
            from capsnet import CapsNetBasic
            model_list = CapsNetBasic(input_shape)
            return model_list
        elif args.net == 'matwo':
            from capsnet import Matwo_CapsNet, MatwoCapsNet
            input_shape = (args.batch_size,) + input_shape
            model_list = Matwo_CapsNet(input_shape, num_labels=num_labels(args.data_root_dir))
            # model.build(input_shape)
            return model_list
        else:
            raise Exception('Unknown network type specified: {}'.format(args.net))
    # If using multiple GPUs
    else:
        with tf.device("/cpu:0"):
            if args.net == 'unet':
                from unet import UNet
                model = UNet(input_shape)
                return [model]
            elif args.net == 'segcapsr1':
                from capsnet import CapsNetR1
                model_list = CapsNetR1(input_shape)
                return model_list
            elif args.net == 'segcapsr3':
                from capsnet import CapsNetR3
                model_list = CapsNetR3(input_shape)
                return model_list
            elif args.net == 'capsbasic':
                from capsnet import CapsNetBasic
                model_list = CapsNetBasic(input_shape)
                return model_list
            elif args.net == 'matwo':
                from capsnet import Matwo_CapsNet
                input_shape = (args.batch_size,) + input_shape
                model_list = Matwo_CapsNet(input_shape, num_labels=num_labels(args.data_root_dir))
                return model_list
            else:
                raise Exception('Unknown network type specified: {}'.format(args.net))
