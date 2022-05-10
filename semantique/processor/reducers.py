import numpy as np
from scipy import stats

from semantique.processor.templates import TYPE_PROMOTION_TEMPLATES

def _is_all_nodata(x, axis):
  return np.equal(np.sum(np.isfinite(x), axis = axis), 0)

def _nodata_as_zero(x):
  return np.nan_to_num(x, nan = 0, posinf = 0, neginf = 0)

#
# NUMERICAL REDUCERS
#

def mean_(x, dimension, track_types = True, **kwargs):
  """Calculate the mean of a set of values.

  Parameters
  ----------
    x : :obj:`xarray.DataArray`
      The data cube to be reduced.
    dimension : :obj:`str`
      Name of the dimension to apply the reduction function to.
    track_types : :obj:`bool`
      Should the reducer promote the value type of the output object, based
      on the value type of the input object?
    **kwargs:
      Ignored.

  Returns
  -------
    :obj:`xarray.DataArray`
      The reduced data cube.

  """
  def f(x, axis, **kwargs):
    return np.nanmean(x, axis = axis)
  out = x.reduce(f, dim = dimension, **kwargs)
  if track_types:
    manual = TYPE_PROMOTION_TEMPLATES["numerical_reducers"]
    out.sq.promote_value_type(x, func = "mean", manual = manual)
  return out

def product_(x, dimension, track_types = True, **kwargs):
  """Calculate the product of a set of values.

  Parameters
  ----------
    x : :obj:`xarray.DataArray`
      The data cube to be reduced.
    dimension : :obj:`str`
      Name of the dimension to apply the reduction function to.
    track_types : :obj:`bool`
      Should the reducer promote the value type of the output object, based
      on the value type of the input object?
    **kwargs:
      Ignored.

  Returns
  -------
    :obj:`xarray.DataArray`
      The reduced data cube.

  """
  def f(x, axis, **kwargs):
    values = np.nanprod(x, axis = axis)
    return np.where(_is_all_nodata(x, axis), np.nan, values)
  out = x.reduce(f, dim = dimension, **kwargs)
  if track_types:
    manual = TYPE_PROMOTION_TEMPLATES["numerical_reducers"]
    out.sq.promote_value_type(x, func = "product", manual = manual)
  return out

def standard_deviation_(x, dimension, track_types = True, **kwargs):
  """Calculate the standard deviation of a set of values.

  Parameters
  ----------
    x : :obj:`xarray.DataArray`
      The data cube to be reduced.
    dimension : :obj:`str`
      Name of the dimension to apply the reduction function to.
    track_types : :obj:`bool`
      Should the reducer promote the value type of the output object, based
      on the value type of the input object?
    **kwargs:
      Ignored.

  Returns
  -------
    :obj:`xarray.DataArray`
      The reduced data cube.

  """
  def f(x, axis, **kwargs):
    return np.nanstd(x, axis = axis)
  out = x.reduce(f, dim = dimension, **kwargs)
  if track_types:
    manual = TYPE_PROMOTION_TEMPLATES["numerical_reducers"]
    out.sq.promote_value_type(x, func = "standard_deviation", manual = manual)
  return out

def sum_(x, dimension, track_types = True, **kwargs):
  """Calculate the sum of a set of values.

  Parameters
  ----------
    x : :obj:`xarray.DataArray`
      The data cube to be reduced.
    dimension : :obj:`str`
      Name of the dimension to apply the reduction function to.
    track_types : :obj:`bool`
      Should the reducer promote the value type of the output object, based
      on the value type of the input object?
    **kwargs:
      Ignored.

  Returns
  -------
    :obj:`xarray.DataArray`
      The reduced data cube.

  """
  def f(x, axis, **kwargs):
    values = np.nansum(x, axis = axis)
    return np.where(_is_all_nodata(x, axis), np.nan, values)
  out = x.reduce(f, dim = dimension, **kwargs)
  if track_types:
    manual = TYPE_PROMOTION_TEMPLATES["numerical_reducers"]
    out.sq.promote_value_type(x, func = "sum", manual = manual)
  return out

def variance_(x, dimension, track_types = True, **kwargs):
  """Calculate the variance of a set of values.

  Parameters
  ----------
    x : :obj:`xarray.DataArray`
      The data cube to be reduced.
    dimension : :obj:`str`
      Name of the dimension to apply the reduction function to.
    track_types : :obj:`bool`
      Should the reducer promote the value type of the output object, based
      on the value type of the input object?
    **kwargs:
      Ignored.

  Returns
  -------
    :obj:`xarray.DataArray`
      The reduced data cube.

  """
  def f(x, axis, **kwargs):
    return np.nanvar(x, axis = axis)
  out = x.reduce(f, dim = dimension, **kwargs)
  if track_types:
    manual = TYPE_PROMOTION_TEMPLATES["numerical_reducers"]
    out.sq.promote_value_type(x, func = "variance", manual = manual)
  return out

#
# BOOLEAN REDUCERS
#

def all_(x, dimension, track_types = True, **kwargs):
  """Test if all values in a set are true.

  Parameters
  ----------
    x : :obj:`xarray.DataArray`
      The data cube to be reduced.
    dimension : :obj:`str`
      Name of the dimension to apply the reduction function to.
    track_types : :obj:`bool`
      Should the reducer promote the value type of the output object, based
      on the value type of the input object?
    **kwargs:
      Ignored.

  Returns
  -------
    :obj:`xarray.DataArray`
      The reduced data cube.

  """
  def f(x, axis, **kwargs):
    values = np.all(x, axis = axis)
    return np.where(_is_all_nodata(x, axis), np.nan, values)
  out = x.reduce(f, dim = dimension, **kwargs)
  if track_types:
    manual = TYPE_PROMOTION_TEMPLATES["boolean_reducers"]
    out.sq.promote_value_type(x, func = "all", manual = manual)
  return out

def any_(x, dimension, track_types = True, **kwargs):
  """Test if at least one value in a set is true.

  Parameters
  ----------
    x : :obj:`xarray.DataArray`
      The data cube to be reduced.
    dimension : :obj:`str`
      Name of the dimension to apply the reduction function to.
    track_types : :obj:`bool`
      Should the reducer promote the value type of the output object, based
      on the value type of the input object?
    **kwargs:
      Ignored.

  Returns
  -------
    :obj:`xarray.DataArray`
      The reduced data cube.

  """
  def f(x, axis, **kwargs):
    return np.any(_nodata_as_zero(x), axis = axis)
  out = x.reduce(f, dim = dimension, **kwargs)
  if track_types:
    manual = TYPE_PROMOTION_TEMPLATES["boolean_reducers"]
    out.sq.promote_value_type(x, func = "any", manual = manual)
  return out

#
# COUNT REDUCERS
#

def count_(x, dimension, track_types = True, **kwargs):
  """Count the number of true values in a set.

  Parameters
  ----------
    x : :obj:`xarray.DataArray`
      The data cube to be reduced.
    dimension : :obj:`str`
      Name of the dimension to apply the reduction function to.
    track_types : :obj:`bool`
      Should the reducer promote the value type of the output object, based
      on the value type of the input object?
    **kwargs:
      Ignored.

  Returns
  -------
    :obj:`xarray.DataArray`
      The reduced data cube.

  """
  def f(x, axis, **kwargs):
    values = np.count_nonzero(_nodata_as_zero(x), axis = axis)
    return np.where(_is_all_nodata(x, axis), np.nan, values)
  out = x.reduce(f, dim = dimension, **kwargs)
  if track_types:
    manual = TYPE_PROMOTION_TEMPLATES["count_reducers"]
    out.sq.promote_value_type(x, func = "count", manual = manual)
  return out

def percentage_(x, dimension, track_types = True, **kwargs):
  """Calculate the percentage of true values in a set.

  Parameters
  ----------
    x : :obj:`xarray.DataArray`
      The data cube to be reduced.
    dimension : :obj:`str`
      Name of the dimension to apply the reduction function to.
    track_types : :obj:`bool`
      Should the reducer promote the value type of the output object, based
      on the value type of the input object?
    **kwargs:
      Ignored.

  Returns
  -------
    :obj:`xarray.DataArray`
      The reduced data cube.

  """
  def f(x, axis, **kwargs):
    part = np.count_nonzero(_nodata_as_zero(x), axis = axis)
    part = np.where(_is_all_nodata(x, axis), np.nan, part)
    whole = np.sum(np.isfinite(x), axis = axis)
    return np.multiply(np.divide(part, whole), 100)
  out = x.reduce(f, dim = dimension, **kwargs)
  if track_types:
    manual = TYPE_PROMOTION_TEMPLATES["count_reducers"]
    out.sq.promote_value_type(x, func = "percentage", manual = manual)
  return out

#
# ORDERED REDUCERS
#

def max_(x, dimension, track_types = True, **kwargs):
  """Return the maximum value in a set.

  Parameters
  ----------
    x : :obj:`xarray.DataArray`
      The data cube to be reduced.
    dimension : :obj:`str`
      Name of the dimension to apply the reduction function to.
    track_types : :obj:`bool`
      Should the reducer promote the value type of the output object, based
      on the value type of the input object?
    **kwargs:
      Ignored.

  Returns
  -------
    :obj:`xarray.DataArray`
      The reduced data cube.

  """
  def f(x, axis, **kwargs):
    return np.nanmax(x, axis = axis)
  out = x.reduce(f, dim = dimension, **kwargs)
  if track_types:
    manual = TYPE_PROMOTION_TEMPLATES["ordered_reducers"]
    out.sq.promote_value_type(x, func = "max", manual = manual)
  return out

def median_(x, dimension, track_types = True, **kwargs):
  """Return the median value in a set.

  Parameters
  ----------
    x : :obj:`xarray.DataArray`
      The data cube to be reduced.
    dimension : :obj:`str`
      Name of the dimension to apply the reduction function to.
    track_types : :obj:`bool`
      Should the reducer promote the value type of the output object, based
      on the value type of the input object?
    **kwargs:
      Ignored.

  Returns
  -------
    :obj:`xarray.DataArray`
      The reduced data cube.

  """
  def f(x, axis, **kwargs):
    return np.nanmedian(x, axis = axis)
  out = x.reduce(f, dim = dimension, **kwargs)
  if track_types:
    manual = TYPE_PROMOTION_TEMPLATES["ordered_reducers"]
    out.sq.promote_value_type(x, func = "median", manual = manual)
  return out

def min_(x, dimension, track_types = True, **kwargs):
  """Return the minimum value in a set.

  Parameters
  ----------
    x : :obj:`xarray.DataArray`
      The data cube to be reduced.
    dimension : :obj:`str`
      Name of the dimension to apply the reduction function to.
    track_types : :obj:`bool`
      Should the reducer promote the value type of the output object, based
      on the value type of the input object?
    **kwargs:
      Ignored.

  Returns
  -------
    :obj:`xarray.DataArray`
      The reduced data cube.

  """
  def f(x, axis, **kwargs):
    return np.nanmin(x, axis = axis)
  out = x.reduce(f, dim = dimension, **kwargs)
  if track_types:
    manual = TYPE_PROMOTION_TEMPLATES["ordered_reducers"]
    out.sq.promote_value_type(x, func = "min", manual = manual)
  return out

#
# UNIVERSAL REDUCERS
#

def first_(x, dimension, track_types = True, **kwargs):
  """Return the first value in a set.

  Parameters
  ----------
    x : :obj:`xarray.DataArray`
      The data cube to be reduced.
    dimension : :obj:`str`
      Name of the dimension to apply the reduction function to.
    track_types : :obj:`bool`
      Should the reducer promote the value type of the output object, based
      on the value type of the input object?
    **kwargs:
      Ignored.

  Returns
  -------
    :obj:`xarray.DataArray`
      The reduced data cube.

  """
  def f(x, axis, **kwargs):
    is_value = np.isfinite(x)
    is_last = np.equal(np.cumsum(np.cumsum(is_value, axis = axis), axis = axis), 1)
    return np.nanmax(np.where(is_last, x, np.nan), axis = axis)
  out = x.reduce(f, dim = dimension, **kwargs)
  if track_types:
    manual = TYPE_PROMOTION_TEMPLATES["universal_reducers"]
    out.sq.promote_value_type(x, func = "first", manual = manual)
  return out

def last_(x, dimension, track_types = True, **kwargs):
  """Return the last value in a set.

  Parameters
  ----------
    x : :obj:`xarray.DataArray`
      The data cube to be reduced.
    dimension : :obj:`str`
      Name of the dimension to apply the reduction function to.
    track_types : :obj:`bool`
      Should the reducer promote the value type of the output object, based
      on the value type of the input object?
    **kwargs:
      Ignored.

  Returns
  -------
    :obj:`xarray.DataArray`
      The reduced data cube.

  """
  def f(x, axis, **kwargs):
    return first_(np.flip(x, axis = axis), axis = axis)
  out = x.reduce(f, dim = dimension, **kwargs)
  if track_types:
    manual = TYPE_PROMOTION_TEMPLATES["universal_reducers"]
    out.sq.promote_value_type(x, func = "last", manual = manual)
  return out

def mode_(x, dimension, track_types = True, **kwargs):
  """Return the most occuring value in a set.

  Parameters
  ----------
    x : :obj:`xarray.DataArray`
      The data cube to be reduced.
    dimension : :obj:`str`
      Name of the dimension to apply the reduction function to.
    track_types : :obj:`bool`
      Should the reducer promote the value type of the output object, based
      on the value type of the input object?
    **kwargs:
      Ignored.

  Returns
  -------
    :obj:`xarray.DataArray`
      The reduced data cube.

  Note
  -------
    If there are multiple modal values in a set, the minimum of them (i.e. the
    smallest of these values) is returned.

  """
  def f(x, axis, **kwargs):
    values = stats.mode(x, axis = axis, nan_policy = "omit")[0].squeeze(axis = axis)
    return np.where(_is_all_nodata(x, axis), np.nan, values)
  out = x.reduce(f, dim = dimension, **kwargs)
  if track_types:
    manual = TYPE_PROMOTION_TEMPLATES["universal_reducers"]
    out.sq.promote_value_type(x, func = "mode", manual = manual)
  return out