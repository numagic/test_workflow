import numpy as np

from unittest import TestCase

class TestSmoke(TestCase):
	def test_selfadd(self):
		assert 1+1 == 2

	def test_casadi_import(self):
		import casadi as cas

	def test_cyipopt_import(self):
		import cyipopt


	def _test_jax_import(self):
		import jax.numpy as jnp