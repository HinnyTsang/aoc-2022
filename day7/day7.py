"""
    AOC 2022 day 7.
    Hinny Tsang
"""

class File():
    """
        class to simulate single file
    """
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

    def calculate_size(self):
        """
            placeholder
        """
        return

    def get_size(self):
        """
            getter for file size
        """
        return self.size

    def get_name(self):
        """
            getter for file name
        """
        return self.name

    def print(self, level = 0):
        """
            print self
        """
        print(f"{'    ' * level}-/{self.name}: {self.size = }")

class FileStructure():
    """
        class to simulate file structure
    """
    def __init__(self, name):
        self.name = name
        self.size = -1
        self.children = {}

    def insert_chird(self, child: File):
        """
            insert chirdren to the current directory.
        """
        self.children[child.get_name()] = child

    def calculate_size(self):
        """
            calculate size of the file structure
        """
        for child in self.children.values():
            child.calculate_size()

        self.size = sum([child.get_size() for child in self.children.values()])

    def get_size(self):
        """
            getter for file size
        """
        if self.size == -1:
            self.calculate_size()
        return self.size

    def get_name(self):
        """
            getter for file name
        """
        return self.name

    def get_child(self, name):
        """
            getter of child
        """
        return self.children[name]

    def has_child(self, name):
        """
            check has subdirectory
        """
        return name in self.children

    def print(self, level = 0):
        """
            print self
        """
        print(f"{'    ' * level}-/{self.name} {self.size = }")
        for child in self.children.values():
            child.print(level + 1)

    def get_limited_size(self, limit):
        """
            get directory size smaller than limit
        """
        result = 0
        if self.get_size() <= limit:
            result += self.get_size()

        for child in self.children.values():
            if isinstance(child, FileStructure):
                result += child.get_limited_size(limit)

        return result

    def get_minimum_folder_to_free(
            self,
            minimum_space_to_free,
            possible_minimum_target_space
        ):
        """
            get minimum directory size to delete
        """
        if minimum_space_to_free <= self.get_size() <= possible_minimum_target_space:
            possible_minimum_target_space = self.get_size()

        for child in self.children.values():
            if isinstance(child, FileStructure):
                possible_minimum_target_space = \
                    child.get_minimum_folder_to_free(
                        minimum_space_to_free,
                        possible_minimum_target_space
                    )

        return possible_minimum_target_space

def construct_file_structure(commands):
    """
        construct the file structure tree base on commands
    """
    dummy = FileStructure('')
    current_folder = dummy
    file_navigator = [dummy]

    for command in commands:
        command = command.strip().split()
        if command[0] == '$':
            if command[1] == 'cd':
                _, _, name = command
                if name == '..':
                    file_navigator.pop()
                    current_folder = file_navigator[-1]

                elif current_folder.has_child(name):
                    child = current_folder.get_child(name)
                    current_folder = child
                    file_navigator.append(current_folder)

                else:
                    child = FileStructure(name)
                    current_folder.insert_chird(child)
                    current_folder = child
                    file_navigator.append(current_folder)

        else:
            info, name = command
            if info == 'dir':
                child = FileStructure(name)
                current_folder.insert_chird(child)
            else:
                child = File(name, info)
                current_folder.insert_chird(child)

    dummy.calculate_size()

    return dummy.get_child('/')

def question7a(file: str) -> None:
    """
        file: input file name
    """
    commands = open(file, 'r', encoding="utf-8").readlines()

    root = construct_file_structure(commands)

    result = root.get_limited_size(100000)

    print(f"{result = }")

def question7b(file: str) -> None:
    """
        file: input file name
    """
    commands = open(file, 'r', encoding="utf-8").readlines()

    root = construct_file_structure(commands)

    total_disk_space = 70000000
    target_unused_space = 30000000
    current_free_space = total_disk_space - root.get_size()
    minimum_space_to_free = target_unused_space - current_free_space

    result = root.get_minimum_folder_to_free(minimum_space_to_free, root.get_size())

    print(f"{result = }")


if __name__ == "__main__":
    FILE_NAME = './input.txt'
    question7a(FILE_NAME)
    question7b(FILE_NAME)
