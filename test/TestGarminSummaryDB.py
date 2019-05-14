#!/usr/bin/env python

#
# copyright Tom Goetz
#

import unittest, logging, os, sys

from TestSummaryDBBase import TestSummaryDBBase

sys.path.append('../.')

import GarminDB


root_logger = logging.getLogger()
handler = logging.FileHandler('garmin_summary_db.log', 'w')
root_logger.addHandler(handler)
root_logger.setLevel(logging.INFO)

logger = logging.getLogger(__name__)
db_dir = os.environ['DB_DIR']


class TestGarminSummaryDB(TestSummaryDBBase, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db_params_dict = {}
        cls.db_params_dict['db_type'] = 'sqlite'
        cls.db_params_dict['db_path'] = db_dir
        db = GarminDB.GarminSummaryDB(cls.db_params_dict)
        super(TestGarminSummaryDB, cls).setUpClass(db,
            {
                'summary_table' : GarminDB.Summary,
                'months_table' : GarminDB.MonthsSummary,
                'weeks_table' : GarminDB.WeeksSummary,
                'days_table' : GarminDB.DaysSummary
            }
        )


if __name__ == '__main__':
    unittest.main(verbosity=2)

