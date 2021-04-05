from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory
from . import db
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os
from PIL import Image

WRITE_FOLDER = ''
USER_NAME = ''

main = Blueprint('main', __name__)

def list_image_names(write_folder, user_name, image_size):
    """Function that retuns a list of images i a folder
    """
    image_dir = f'{write_folder}/{user_name}/{image_size}'
    # print('image_dir',image_dir)
    return os.listdir(image_dir)

def write_thumbnail(image_name, size):
    """ creates a thumbnail image of the size from the image name passed 
    """
    # TODO : use something else instead of image.thumbnail
    sizes = {
        'small' : [30,40],
        'medium' : [70,70],
        'large' : [120,120]
    }
    image = Image.open(f'{WRITE_FOLDER}/{USER_NAME}/original/{image_name}')
    image.thumbnail((sizes[size][0], sizes[size][1]))
    image.save(f'{WRITE_FOLDER}/{USER_NAME}/{size}/{image_name}')

def create_thumbnail(image_name):
    """Creates thumbnails of small, medium and large sizes for the given image
    """
    try:
        # SMALL
        write_thumbnail(image_name, 'small')
        # MEDIUM
        write_thumbnail(image_name, 'medium')
        # LARGE
        write_thumbnail(image_name, 'large')

    except IOError:
        print('create thumbnail error')
        pass

# PAGE ROUTES
@main.route('/')
def index():
    # try:
    #     print(current_user.__dict__)
    # except:
    #     print('user not found')
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    # TODO : move this to index ?
    global WRITE_FOLDER
    global USER_NAME
    WRITE_FOLDER = 'project/images/'
    USER_NAME = current_user.name
    return render_template('profile.html', user_name = USER_NAME )


@main.route('/upload')
@login_required
def upload_page():
    return render_template('upload.html')

@main.route('/upload', methods=['POST'])
@login_required
def upload_image():
    uploaded_file = request.files['uploaded_file']
    save_directory = f'{WRITE_FOLDER}{USER_NAME}/original/{secure_filename(uploaded_file.filename)}'
    print(f'save directory {save_directory}')
    uploaded_file.save(save_directory)
    print(f'Current directory {os.getcwd()}')
    create_thumbnail(secure_filename(uploaded_file.filename))
    return redirect(url_for('main.list_images'))

@main.route('/listimg')
@login_required
def list_images():
    user_name = current_user.name
    image_list = list_image_names(WRITE_FOLDER, USER_NAME, 'original')
    # print(f'write folder {WRITE_FOLDER}, images {image_list} ')
    return render_template('view_image.html', filenames=image_list)

@main.route('/get_image/<filename>/<size>')
def get_image(filename, size):
    size = size
    # print(f'size of image fetched {size}')
    return send_from_directory(f'images/{USER_NAME}/{size}', filename = filename)

@main.route('/get_image_sizes/<filename>')
def get_image_sizes(filename):
    # return send_from_directory(f'images/{USER_NAME}', filename = filename)
    return render_template('view-image_sizes.html', filename=filename)

@main.route('/download-image/<filename>/<size>')
def download_image(filename, size):
    size = size
    print('download of image fetched {size}')
    return send_from_directory(f'images/{USER_NAME}/{size}', filename = filename, as_attachment=True)

