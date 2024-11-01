from enum import Enum

class ProjectStatus(Enum):
    ACTIVE = 'Active'
    IN_PROGRESS = 'In Progress'
    INACTIVE = 'Inactive'
    DELETED = 'Deleted'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class Platform(Enum):
    WEB = 'Web'
    MOBILE = 'Mobile'
    DESKTOP = 'Desktop'
    WEB_MOBILE = 'Web and Mobile'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class Framework(Enum):
    DJANGO = 'Django'
    FLASK = 'Flask'
    FASTAPI = 'FastAPI'
    DJANGO_REST = 'Django REST'
    DJANGO_GRAPHQL = 'Django GraphQL'
    NEXT_JS = 'Next.js'
    REACT_JS = 'React.js'
    ANGULAR = 'Angular'
    VUE_JS = 'Vue.js'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]