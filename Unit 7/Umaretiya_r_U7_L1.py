''' Test cases:
6 https://cf.geekdo-images.com/imagepage/img/5lvEWGGTqWDFmJq_MaZvVD3sPuM=/fit-in/900x600/filters:no_upscale()/pic260745.jpg
10 cute_dog.jpg
6 turtle.jpg
'''
import PIL
from PIL import Image
import urllib.request
import io, sys, os, random

def choose_random_means(k, img, pix):
   return [pix[(int)(random.uniform(0, img.size[0]-1)),(int)(random.uniform(0, img.size[1]-1))] for i in range(k)]

# goal test: no hopping
def check_move_count(mc):
   for move in mc:
      if move != 0: return False
   return True

# calculate distance with the current color with each mean
# return the index of means
def dist(col, means):
   minIndex, dist_sum = 0, 255 ** 2 + 255 ** 2 + 255 ** 2
   for i in range(len(means)):
      dist_k = ((means[i][0]-col[0]) ** 2 + (means[i][1]-col[1])**2 + (means[i][2]-col[2])**2) ** 0.5
      if dist_k < dist_sum:
         dist_sum = dist_k
         minIndex = i
   return minIndex 

def clustering(img, pix, cb, mc, means, count):
   temp_pb, temp_mc, temp_m = [[] for x in means], [], []
   temp_cb = [0 for x in range(len(means))]
   
   for tup in rgb: 
      temp_cb[dist(tup, means)] += 1
      temp_pb[dist(tup, means)].append(tup)
   
   temp_mc = [(a - b) for a, b in zip(temp_cb, cb)]
   for li in temp_pb:
      sum_r, sum_g, sum_b = 0, 0, 0
      for tup in li:
         sum_r += tup[0]
         sum_g += tup[1]
         sum_b += tup[2]
      temp_m.append((sum_r / len(li), sum_g / len(li), sum_b / len(li)))
   print ('diff', count, ':', temp_mc)
   return temp_cb, temp_mc, temp_m

def update_picture(img, pix, means):
   region_dict = {}
   return pix, region_dict
   
def distinct_pix_count(img, pix):
   cols = {}
   max_col, max_count = pix[0, 0], 0
   return len(cols.keys()), max_col, max_count

def count_regions(img, region_dict, pix, means):
   region_count = [0 for x in means]
   return region_count

 
def main():
   k = int(sys.argv[1])
   file = sys.argv[2]
   if not os.path.isfile(file):
      file = io.BytesIO(urllib.request.urlopen(file).read())
   img = Image.open(file)
   pix = img.load()   # pix[0, 0] : (r, g, b) 
   print ('Size:', img.size[0], 'x', img.size[1])
   print ('Pixels:', img.size[0]*img.size[1])
   d_count, m_col, m_count = distinct_pix_count(img, pix)
   print ('Distinct pixel count:', d_count)
   print ('Most common pixel:', m_col, '=>', m_count)

   count_buckets = [0 for x in range(k)]
   move_count = [10 for x in range(k)]
   means = choose_random_means(k, img, pix)
   print ('random means:', means)
   count = 1
   while not check_move_count(move_count):
      count += 1
      count_buckets, move_count, means = clustering(img, pix, count_buckets, move_count, means, count)
      if count == 2:
         print ('first means:', means)
         print ('starting sizes:', count_buckets)
   pix, region_dict = update_picture(img, pix, means)
   print ('Final sizes:', count_buckets)
   print ('Final means:')
   for i in range(len(means)):
      print (i+1, ':', means[i], '=>', count_buckets[i])
   regions = count_regions(img, region_dict, pix, means)  #  num of area fills
   print ('Region counts:', regions)
   img.save('output.png', 'PNG')


   '''
   Distinct regions:
      1: # of regions of means[0]
   Final regions:
      1: # of final regions of means[0] after taking care of step 3
   Save your file in the subdirectory, kmeans/userid.png
   '''
   img.show()
   
if __name__ == '__main__': 
   main()