class JSON:

    @classmethod
    def to_json(cls, object_) -> str:
        content = cls.form_dict(object_)
        return cls.to_string(content)