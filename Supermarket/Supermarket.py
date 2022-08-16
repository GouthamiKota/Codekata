class Super/market(object):
  @staticmethod
  def get_can_of_bean_price():
    return 0.65
  @staticmethod
  def cost(number_of_can):
    if number_of_can==3:
      return 1.0
    else:
      return number_of_can*0.65
