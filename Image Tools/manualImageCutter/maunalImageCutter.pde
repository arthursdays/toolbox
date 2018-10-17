ArrayList<String> rawPhotos = new ArrayList<String>();
int windowSize = 122;
int index = 0;
PImage aPhoto;
int left, right, top, bottom;
File srcFolder, dstFolder;

String photoName;
float ratio = 1.0;

boolean overImg = false;
boolean locked = false;
int mouseDraggedX = 0;
int mouseDraggedY = 0;

int dx = 0;
int dy = 0; 

void setup() {
  size(1440, 900);
  srcFolder = new File("C:\\Users\\Arthur\\Desktop\\yinxiebing\\bystage\\JinZhanQiBanKuai");
  dstFolder = new File("C:\\Users\\Arthur\\Desktop\\yinxiebing\\bystage\\JinZhanQiBanKuai\\precise");
  for (final File afile : srcFolder.listFiles())
  {
    rawPhotos.add(afile.getAbsolutePath());
  }
  
  photoName = rawPhotos.get(0);
  aPhoto = loadImage(photoName);
}

void draw()
{
  background(80, 255, 20);

  float yr = aPhoto.height*ratio;
  float xr = aPhoto.width*ratio;
  image(aPhoto, dx, dy, xr, yr);
  //rectMode(CENTER);
  left = mouseX-windowSize/2;
  right = mouseX+windowSize/2;
  top = mouseY-windowSize/2;
  bottom = mouseY+windowSize/2;

  if (left <= max(0, dx))
    left = max(0, dx);
  if (right >= min(width, dx + xr))
    left = int(min(width, dx + xr)) - windowSize;
  if (top <= max(0, dy))
    top = max(0, dy);
  if (bottom >= min(height, dy + yr))
    top = int(min(height, dy + yr)) - windowSize;

  if (left > max(0, dx) && right < min(width, dx + xr) && 
    top > max(0, dy) && bottom < min(height, dy + yr)) {
    overImg = true;  
    if (!locked) { 
      stroke(255, 0, 0);
    }
  } else {
    stroke(0, 255, 255);
    overImg = false;
  }

  rect(left, top, windowSize, windowSize);
  noFill();
}

void mouseClicked()
{
  if (mouseButton == LEFT)
  {
    if (!locked) {
      PImage toSave = createImage(windowSize, windowSize, RGB);
      toSave.copy(get(left, top, windowSize, windowSize), 0, 0, windowSize, windowSize, 0, 0, windowSize, windowSize);
      String namePart = split(split(photoName, "\\")[split(photoName, "\\").length-1], ".")[0];
      toSave.save(dstFolder.getAbsolutePath()+"\\"+namePart+"_at("+top+","+left+")"+".jpg");
    }
  }
  if (mouseButton == RIGHT)
  {
    index++;
    photoName = rawPhotos.get(index);
    aPhoto = loadImage(photoName);
    ratio = 1;
    dx = 0;
    dy = 0;
    mouseDraggedX = 0;
    mouseDraggedY = 0;
  }
}

void mousePressed()
{
  if (overImg) { 
    locked = true;
  } else {
    locked = false;
  }
  mouseDraggedX = mouseX-dx; 
  mouseDraggedY = mouseY-dy;
}

void mouseWheel(MouseEvent e) 
{
  float value = e.getCount();
  println(value);
  ratio -= value/10.0;
}

void mouseDragged()
{
  if (locked) {
    dx = mouseX-mouseDraggedX; 
    dy = mouseY-mouseDraggedY;
  }
}

void mouseReleased() {
  locked = false;
}
