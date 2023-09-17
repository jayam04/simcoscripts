class Building:
    def __init__(self, id, kind, name, size, robots_specialization=None, pinned_resource=None) -> None:
        self.id = id
        self.kind = kind
        self.name = name
        self.size = size
        self.robots_specialization = robots_specialization
        self.pinned_resource = pinned_resource

    def __str__(self):
        # TODO: better string which included pinned resource and robot specialization if it's there
        return f"{self.name} ({self.id}) of size {self.size} and kind {self.kind}"
