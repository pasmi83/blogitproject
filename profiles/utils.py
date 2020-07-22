from PIL import Image
from django.conf import settings
import sys

#def generate_profile_+nail(profile_id, filename, w, h):
def generate_profile_thumbnail(profile_id, file, w, h):
    
    thumb = Image.open(file)
    #thumb.thumbnail((w, h), Image.ANTIALIAS)
    old_w = thumb.size[0]
    old_h = thumb.size[1]
    print('OLD: ',old_w,old_h)
    new_h = (int(old_h)/int(old_w))*w
    print('NEW: ',new_h)
    thumb.thumbnail((w,new_h), Image.ANTIALIAS)
    thumb = thumb.convert('RGB')
    #thumb_filename = filename.split("/")[-1]
    thumb_filename = file.name.split("/")[-1]
    
    thumb_file_path = 'profile_thumbs/{}'.format('thumb_' + str(profile_id) + '_' + thumb_filename)
    
    print (thumb_file_path)
    thumb.save('media/' + thumb_file_path,'JPEG')
    #profile_image_thumbnail.save('media/' + thumb_file_path)
    
    return thumb_file_path
