import sys
import dropbox
from dropbox import sharing

from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError

# Access token
from dropbox.sharing import AccessLevel, SharedLinkSettings, RequestedLinkAccessLevel

DROPBOX_TOKEN = 'kapSGxRhofAAAAAAAAAADmdBKmkCUzSnp7UBiCkiM3CPsGygDpF3eBmoI_d6wyvh'


def create_public_link(file_name):
    try:
        path = './' + file_name

        dropbox_api = dropbox.Dropbox(DROPBOX_TOKEN)

        get_shared_links = dropbox_api.sharing_list_shared_links(path=path)

        for shared_link in get_shared_links.links:
            dropbox_api.sharing_revoke_shared_link(url=shared_link.url)

        sharing_setting = SharedLinkSettings(access=sharing.RequestedLinkAccessLevel.viewer)
        response = dropbox_api.sharing_create_shared_link_with_settings(path='/uploaded.pdf', settings=sharing_setting)
        return response.url
    except Exception as e:
        print(str(e))
        return None


def upload_file(path, file_name):
    try:
        with open(path, 'rb') as local_file:
            dropbox_path = './' + file_name
            dropbox_api = dropbox.Dropbox(DROPBOX_TOKEN)

            response = dropbox_api.files_upload(local_file.read(), dropbox_path, mode=WriteMode('overwrite'))
            return response

    except ApiError as err:

        if (err.error.is_path() and
                err.error.get_path().error.is_insufficient_space()):

            sys.exit("ERROR: Cannot back up; insufficient space.")

        elif err.user_message_text:

            print(err.user_message_text)

            sys.exit()

        else:

            print(err)

            sys.exit()

    except Exception as e:
        print(str(e))

    return None


def delete_file(file_name):
    try:
        dropbox_path = './' + file_name
        dropbox_api = dropbox.Dropbox(DROPBOX_TOKEN)

        response = dropbox_api.files_delete(dropbox_path)
        return response

    except Exception as e:
        print(str(e))
        return None


def upload_and_get_url(path, file_name):
    upload_file(path=path, file_name=file_name)
    url = create_public_link(file_name=file_name)
    return url
