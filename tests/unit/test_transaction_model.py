from unittest import TestCase

from app.models.transaction import TransactionModel


class TestTransactionModel(TestCase):
    def test_id_should_be_auto_created(self):
        model = TransactionModel(artist='Artist')
        self.assertTrue(hasattr(model, 'id'))

    def test_id_should_be_unique(self):
        ids = [TransactionModel(artist=f'Artist {i}').id for i in range(50)]
        self.assertEqual(len(ids), len(set(ids)), 'Id must be always unique')
