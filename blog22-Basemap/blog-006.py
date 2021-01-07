# -*- coding: cp936 -*-
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

width = 28000000; lon_0 = -105; lat_0 = 40
m = Basemap(width=width,height=width,projection='aeqd',
            lat_0=lat_0,lon_0=lon_0)

# ��䱳��
m.drawmapboundary(fill_color='aqua')
# ���ƺ����߲�����½
m.drawcoastlines(linewidth=0.5)
m.fillcontinents(color='coral',lake_color='aqua')
# 20�Ⱦ�γ�ȣ���Χ-80��81 -180��180
m.drawparallels(np.arange(-80,81,20))
m.drawmeridians(np.arange(-180,180,20))
# �����Ļ���һ���ڵ�
xpt, ypt = m(lon_0, lat_0)
m.plot([xpt],[ypt],'ko')
# ���Ʊ���
plt.title('Azimuthal Equidistant Projection')
plt.show()
