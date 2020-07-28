# 4.4 Qt程序

基于python的俄罗斯方块程序

## Tetris对象

Tetris对象中包含的界面设置，包括界面大小以及设置在屏幕中央

## Board对象

Board对象中定义的游戏的玩法，包括消除完整的一行、游戏按键设置、方块移动操作和方块在面板上的定位等。

* tryMove
  
  移动操作函数要判断下一个情况的方块是否处在面板内，以及是否与别的方块相碰了，若没有返回True执行移动操作。
  
  bug：在面板边缘无法进行方块旋转操作
  ```
  def tryMove(self, newPiece, newX, newY):

        for i in range(4):

            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i)

            if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
                return False

            if self.shapeAt(x, y) != Tetrominoe.NoShape:
                return False

        self.curPiece = newPiece
        self.curX = newX
        self.curY = newY
        self.update()

        return True
  ```

##Tetrominoe对象

将俄罗斯方块的形状定义为枚举变量，存储在这个类中

## Shape对象

* coordsTable中定义了8种形状的俄罗斯方块，每种形状的俄罗斯方块都可以用4个小方块通过不同组合形式构成。
  通过设置二维坐标轴，来设置四个小方块的坐标位置，从而定义每个形状。
  
  ```python
  coordsTable = (
        ((0, 0), (0, 0), (0, 0), (0, 0)),
        ((0, -1), (0, 0), (-1, 0), (-1, 1)),
        ((0, -1), (0, 0), (1, 0), (1, 1)),
        ((0, -1), (0, 0), (0, 1), (0, 2)),
        ((-1, 0), (0, 0), (1, 0), (0, 1)),
        ((0, 0), (1, 0), (0, 1), (1, 1)),
        ((-1, -1), (0, -1), (0, 0), (0, 1)),
        ((1, -1), (0, -1), (0, 0), (0, 1))
    )
  ```
  
* 左旋转
  根据上面的形状坐标，往左旋转可以看成是先通过y=x镜像翻转后，再通过y轴镜像翻转

  ```
  def rotateLeft(self):

        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape

        for i in range(4):
            result.setX(i, self.y(i))
            result.setY(i, -self.x(i))

        return result
  ```
  
* 右旋转
  通过y=x镜像翻转后，再通过x轴镜像翻转

  ```
   def rotateRight(self):

        if self.pieceShape == Tetrominoe.SquareShape:
            return self

        result = Shape()
        result.pieceShape = self.pieceShape

        for i in range(4):
            result.setX(i, -self.y(i))
            result.setY(i, self.x(i))

        return result
  ```
## GUI
![Tetris_gui](https://github.com/Ramdoo/2020/blob/master/graph4README/Tetris_ui.png)


## 未完成：

* 通过pyinstaller打包成exe文件运行

* 通过交叉编译在arm上运行
