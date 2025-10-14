import subprocess

def check_brightnessctl():
    """
    :return True if brightnessctl is installed, else : False
    """
    try:
        subprocess.run(['brightnessctl', '--version'],
                       capture_output=True, #capture the output so if it does not work,
                       #gives a CalledProcessError
                       check=True) #Extra security check
        return True

    except (FileNotFoundError, subprocess.CalledProcessError):
        print("You do not have brightnessctl installed on your computer, you can install "
              "it from your package manager. Or you may have an issue with it, try"
              " to fix it before rerunning the app.")
        return False

def get_max_brightness_non_percentage():
    """
    :return the maximum amount of brightness not in % format
    """
    try:
        maxi = subprocess.run(['brightnessctl', 'max'],
                       capture_output=True,
                       text=True,
                       check=True)
        return int(maxi.stdout.strip())

    except subprocess.CalledProcessError:
        print(f"Error: brightnessctl command failed")
        return None

    except (ValueError, AttributeError) as e:
        print(f"Error converting brightness value: {e}")
        return None

    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def get_current_brightness_non_percentage():
    """
    :return the current amount of brightness not in % format
    """
    try:
        current = subprocess.run(['brightnessctl', 'get'],
                       capture_output=True,
                       text=True,
                       check=True)
        return int(current.stdout.strip())

    except subprocess.CalledProcessError:
        print(f"Error: brightnessctl command failed")
        return None

    except (ValueError, AttributeError) as e:
        print(f"Error converting brightness value: {e}")
        return None

    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def show_brightness_percentage():
    """
    :return the value of the current brightness in %. None if failed
    """
    maxi = get_max_brightness_non_percentage()
    current = get_current_brightness_non_percentage()

    if maxi is None or current is None:
        return None

    if maxi == 0:
        return None

    percentage = round((current / maxi) * 100)
    return percentage


def set_brightness(value : int):
    """
    :param value : an integer between 0 and 100
    :return change the luminosity using brightnessctl set <value>
    """
    try:
        percentage = value
        if value < 1: # Avoiding a black screen so minimal value is 1%
            percentage = 1
        elif value > 100:
            percentage = 100
        subprocess.run(['brightnessctl', 'set', f'{percentage}%'],
                       check=True)
        return 0 #succes

    except PermissionError as e:
        print(f"Error: Insufficient permissions : {e}. Try running the app as sudo.")
        return 1 #Failed

    except subprocess.CalledProcessError as e:
        print(f"Error: brightnessctl command failed : {e}")
        return 1

    except Exception as e:
        print(f"Unexpected error: {e}")
        return 1