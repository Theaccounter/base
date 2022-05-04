class BaseService:

    def __init__(self, **kwargs):
        kwargs.setdefault("context", {})
        for key, value in kwargs.items():
            setattr(self, key, value)
        if not isinstance(self.context, dict):
            raise TypeError(f"invalid type of `context` must be a dict"
                            f" received {type(self.context)}")
