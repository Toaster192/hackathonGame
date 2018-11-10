import src.Config as Config

L = ((0, 0),
     (1 * Config.BLOCK_WIDTH, 0),
     (2 * Config.BLOCK_WIDTH, 0),
     (0, 1 * Config.BLOCK_WIDTH))
L1 = ((0, 0),
      (0, 1 * Config.BLOCK_WIDTH),
      (0, 2 * Config.BLOCK_WIDTH),
      (1 * Config.BLOCK_WIDTH,
       2 * Config.BLOCK_WIDTH))
L2 = ((0,
       1 * Config.BLOCK_WIDTH),
      (1 * Config.BLOCK_WIDTH,
       1 * Config.BLOCK_WIDTH),
      (2 * Config.BLOCK_WIDTH,
       1 * Config.BLOCK_WIDTH),
      (2 * Config.BLOCK_WIDTH, 0))
L3 = ((0, 0),
      (1 * Config.BLOCK_WIDTH, 0),
      (1 * Config.BLOCK_WIDTH,
       1 * Config.BLOCK_WIDTH),
      (1 * Config.BLOCK_WIDTH,
       2 * Config.BLOCK_WIDTH))
J = ((0, 0),
     (0, 1 * Config.BLOCK_WIDTH),
     (1 * Config.BLOCK_WIDTH,
      1 * Config.BLOCK_WIDTH),
     (2 * Config.BLOCK_WIDTH,
      1 * Config.BLOCK_WIDTH))
J1 = ((1 * Config.BLOCK_WIDTH, 0),
      (1 * Config.BLOCK_WIDTH,
       1 * Config.BLOCK_WIDTH),
      (1 * Config.BLOCK_WIDTH,
       2 * Config.BLOCK_WIDTH),
      (0, 2 * Config.BLOCK_WIDTH))
J2 = ((0, 0),
      (1 * Config.BLOCK_WIDTH, 0),
      (2 * Config.BLOCK_WIDTH, 0),
      (2 * Config.BLOCK_WIDTH,
       1 * Config.BLOCK_WIDTH))
J3 = ((0, 0),
      (1 * Config.BLOCK_WIDTH, 0),
      (0, 1 * Config.BLOCK_WIDTH),
      (0, 2 * Config.BLOCK_WIDTH))
SQR = ((0, 0),
       (0, 1 * Config.BLOCK_WIDTH),
       (1 * Config.BLOCK_WIDTH, 0),
       (1 * Config.BLOCK_WIDTH,
        1 * Config.BLOCK_WIDTH))
S = ((0, 0),
     (0, 1 * Config.BLOCK_WIDTH),
     (1 * Config.BLOCK_WIDTH,
      1 * Config.BLOCK_WIDTH),
     (1 * Config.BLOCK_WIDTH,
      2 * Config.BLOCK_WIDTH))
S1 = ((1 * Config.BLOCK_WIDTH, 0),
      (2 * Config.BLOCK_WIDTH, 0),
      (0, 1 * Config.BLOCK_WIDTH),
      (1 * Config.BLOCK_WIDTH,
       1 * Config.BLOCK_WIDTH))
Z = ((0, 0),
     (1 * Config.BLOCK_WIDTH, 0),
     (1 * Config.BLOCK_WIDTH,
      1 * Config.BLOCK_WIDTH),
     (2 * Config.BLOCK_WIDTH,
      1 * Config.BLOCK_WIDTH))
Z1 = ((1 * Config.BLOCK_WIDTH, 0),
      (1 * Config.BLOCK_WIDTH,
       1 * Config.BLOCK_WIDTH),
      (0, 1 * Config.BLOCK_WIDTH),
      (0, 2 * Config.BLOCK_WIDTH))
LINE = ((0, 0),
        (0, 1 * Config.BLOCK_WIDTH),
        (0, 2 * Config.BLOCK_WIDTH),
        (0, 3 * Config.BLOCK_WIDTH))
LINE2 = ((0, 0),
         (1 * Config.BLOCK_WIDTH, 0),
         (2 * Config.BLOCK_WIDTH, 0),
         (3 * Config.BLOCK_WIDTH, 0))
T = ((0, 0),
     (0, 1 * Config.BLOCK_WIDTH),
     (0, 2 * Config.BLOCK_WIDTH),
     (1 * Config.BLOCK_WIDTH,
      1 * Config.BLOCK_WIDTH))
T1 = ((0, 0),
      (1 * Config.BLOCK_WIDTH, 0),
      (2 * Config.BLOCK_WIDTH, 0),
      (1 * Config.BLOCK_WIDTH,
       1 * Config.BLOCK_WIDTH))
T2 = ((0, 1 * Config.BLOCK_WIDTH),
      (1 * Config.BLOCK_WIDTH,
       1 * Config.BLOCK_WIDTH),
      (1 * Config.BLOCK_WIDTH, 0),
      (1 * Config.BLOCK_WIDTH,
       2 * Config.BLOCK_WIDTH))
T3 = ((1 * Config.BLOCK_WIDTH, 0),
      (1 * Config.BLOCK_WIDTH,
       1 * Config.BLOCK_WIDTH),
      (0, 1 * Config.BLOCK_WIDTH),
      (2 * Config.BLOCK_WIDTH,
       1 * Config.BLOCK_WIDTH))

array = (L, L1, L2, L3,    J,   J1,    J2,    J3, SQR, SQR,  S,  S, S1, S1,
         Z,  Z, Z1, Z1, LINE, LINE, LINE2, LINE2,   T,  T1, T2, T3)
