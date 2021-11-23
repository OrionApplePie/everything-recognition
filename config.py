
SUB_FACE_CASCADES = {
    'Smile': {
        'path': 'haarcascades/faces/haarcascade_smile.xml',
        'color': (0, 255, 0),
        'draw': True,
    },
    'Eyes': {
        'path': 'haarcascades/faces/haarcascade_eye.xml',
        'color': (0, 0, 255),
        'draw': True,
    },
}

CASCADES = {
    'Face front': {
        'path': 'haarcascades/faces/haarcascade_frontalface_default.xml',
        'color': (255, 0, 0),
        'draw': True,
        'sub_cascades': SUB_FACE_CASCADES,
    },
    'Face profile': {
        'path': 'haarcascades/faces/haarcascade_profileface.xml',
        'color': (255, 0, 0),
        'draw': True,
        'sub_cascades': SUB_FACE_CASCADES,
    },
    'Full body': {
        'path': 'haarcascades/faces/haarcascade_fullbody.xml',
        'color': (0, 255, 0),
        'draw': False
    },
    'Cat face': {
        'path': 'haarcascades/faces/haarcascade_frontalcatface_extended.xml',
        'color': (0, 255, 0),
        'draw': False
    }
}