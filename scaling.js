function to_scale (x, x_min, x_max, y_min, y_max, round_to = 0) {
  const x_coeff = (x_max - x_min) / (y_max - y_min),
        y_diff = (x - x_min) / x_coeff, 
        y = y_min + y_diff,
        y_round = y.toFixed(round_to);
  return y_round;
}
