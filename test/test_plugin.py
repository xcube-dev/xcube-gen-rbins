import unittest

from xcube.util import extension

from xcube_gen_rbins.plugin import init_plugin


class RbinsPluginTest(unittest.TestCase):

    # noinspection PyMethodMayBeStatic
    def test_init_plugin(self):
        ext_reg = extension.ExtensionRegistry()
        init_plugin(ext_reg)
        self.assertTrue(ext_reg.has_extension('xcube.core.gen.iproc', 'rbins-seviri-highroc-daily-l2'))
        self.assertTrue(ext_reg.has_extension('xcube.core.gen.iproc', 'rbins-seviri-highroc-scene-l2'))
