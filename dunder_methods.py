from protocol_example.app import models


class Model:
    def __init__(self, value: int) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"Model({self.value})"

    def __eq__(self, __value: object) -> bool:
        if __value == None or not isinstance(__value, Model):
            return False
        return self.value == __value.value

    def __lt__(self, __value: object) -> bool:
        if __value == None or not isinstance(__value, Model):
            return False
        return self.value < __value.value

    def __gt__(self, __value: object) -> bool:
        if __value == None or not isinstance(__value, Model):
            return False
        return self.value > __value.value

    def __le__(self, __value: object) -> bool:
        if __value == None or not isinstance(__value, Model):
            return False
        return self.value <= __value.value

    def __ge__(self, __value: object) -> bool:
        if __value == None or not isinstance(__value, Model):
            return False
        return self.value >= __value.value

    def __ne__(self, __value: object) -> bool:
        if __value == None or not isinstance(__value, Model):
            return False
        return self.value != __value.value

    def __hash__(self) -> int:
        return hash(self.value)


class ModelListIterator:

    def __init__(self, models: list[Model]) -> None:
        self.index = 0
        self._models = models

    def __next__(self) -> Model:
        if self.index < len(self._models):
            model = self._models[self.index]
            self.index += 1
            return model
        raise StopIteration


class ModelList:

    def __init__(self, *models: Model) -> None:
        self._models = []
        self._models.extend(models)

    def __repr__(self) -> str:
        return f"ModelList({self._models})"

    def __iter__(self):
        return ModelListIterator(self._models)

    def __getitem__(self, index: int) -> Model:
        if index >= 0 and index <= len(self._models):
            return self._models[index]
        raise IndexError("Index out of range")

    def __setitem__(self, index: int, value: Model) -> None:
        if index >= 0 and index <= len(self._models):
            self._models[index] = value
            return
        raise IndexError("Index out of range")


if __name__ == '__main__':
    modelList = ModelList(Model(1), Model(2), Model(3))
    print(modelList)
    modelList[0] = Model(4)
    print(modelList)
