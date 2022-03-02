from sqlalchemy.orm import Session

from app.models.revenue import Revenue


class CURDRevenue(object):
    def __init__(self, model):
        self._model = model

    def create(self, db_postgres, request) -> Revenue:
        print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
        print(self._model)
        print(db_postgres)
        print(request)
        # db_revenue = Revenue()
        self._model.amount = request.amount
        self._model.source = request.source
        self._model.regular = request.regular
        self._model.id_bank = request.id_bank
        self._model.note = request.note

        db_postgres.add(self._model)
        db_postgres.commit()
        db_postgres.refresh(self._model)

        return self._model


revenue = CURDRevenue(Revenue())
