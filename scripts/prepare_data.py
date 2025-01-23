from keras.preprocessing.image import ImageDataGenerator

def get_train_val_generators(train_dir, val_dir, batch_size):
    """
    Create the training and validation data generators for the model.
    """
    # Increaing the dimensions of the image
    train_datagen = ImageDataGenerator(
        rescale=1/255, 
        shear_range=0.2, 
        zoom_range=0.2, 
        horizontal_flip=True)
    val_datagen = ImageDataGenerator(rescale=1./255)
    
    train_generator = train_datagen.flow_from_directory(train_dir, target_size=(224,224), batch_size=batch_size, class_mode='binary')
    val_generator = val_datagen.flow_from_directory(val_dir, target_size=(224,224), batch_size=batch_size, class_mode='binary')
    
    return train_generator, val_generator