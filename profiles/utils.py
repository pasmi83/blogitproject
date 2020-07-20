from PIL import Image

#def generate_profile_thumbnail(profile_id, filename, w, h):
def generate_profile_thumbnail(profile_id, file, w, h):
    
    thumb = Image.open(file)
    #thumb.thumbnail((w, h), Image.ANTIALIAS)
    thumb.thumbnail((w, h), Image.ANTIALIAS)
    #thumb_filename = filename.split("/")[-1]
    thumb_filename = file.name.split("/")[-1]
    
    thumb_file_path = 'profile_thumbs/{}'.format('thumb_' + str(profile_id) + '_' + thumb_filename)
    print (thumb)
    thumb.save('media/' + thumb_file_path,'JPEG')
    #profile_image_thumbnail.save('media/' + thumb_file_path)
    
    return thumb
