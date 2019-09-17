import os
import unittest

from test.helpers import get_inputdata_path
from xcube.api.gen.gen import gen_cube
from xcube.util.dsio import rimraf


def clean_up():
    files = ['l2c-single.nc', 'l2c.nc', 'l2c.zarr']
    for file in files:
        rimraf(os.path.join('.', file))
        rimraf(os.path.join('.', file + 'temp.nc'))


class RbinsProcessTest(unittest.TestCase):

    def setUp(self):
        clean_up()

    def tearDown(self):
        clean_up()

    # noinspection PyMethodMayBeStatic
    def test_process_inputs_single(self):
        status = process_inputs_wrapper(
            input_paths=[get_inputdata_path('SEVIRI_SNS_EUR_201708060700_QV_2013b.1_v02.nc')],
            output_path='l2c-single.nc',
            output_writer='netcdf4',
            append_mode=False)
        self.assertEqual(True, status)

    def _test_process_inputs_append_multiple_nc(self):
        status = process_inputs_wrapper(
            input_paths=[get_inputdata_path('SEVIRI_SNS_EUR_201708060715_QV_2013b.1_v02.nc')],
            output_path='l2c.nc',
            output_writer='netcdf4',
            append_mode=True)
        self.assertEqual(True, status)

    def test_process_inputs_append_multiple_zarr(self):
        status = process_inputs_wrapper(
            input_paths=[get_inputdata_path('SEVIRI_SNS_EUR_201708060730_QV_2013b.1_v02.nc')],
            output_path='l2c.zarr',
            output_writer='zarr',
            append_mode=True)
        self.assertEqual(True, status)


# noinspection PyShadowingBuiltins
def process_inputs_wrapper(input_paths=None,
                           output_path=None,
                           output_writer='netcdf4',
                           append_mode=False):
    return gen_cube(input_paths=input_paths, input_processor_name='rbins-seviri-highroc-scene-l2',
                    output_region=(-4., 47., 12., 56.), output_size=(320, 180), output_resampling='Nearest',
                    output_path=output_path, output_writer_name=output_writer,
                    output_variables=[('KPAR', None), ('SPM', None), ('TUR', None)], append_mode=append_mode,
                    dry_run=False, monitor=None)
