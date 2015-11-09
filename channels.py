import time
import simplejson
from channel import BaseChannel, ChannelException,ChannelMetaClass, STATUS_BAD, STATUS_GOOD, STATUS_UGLY
from utils import *

#############
## Arirang ##
#############

class Arirang(BaseChannel):
    playable = True
    short_name = 'arirang_world'
    long_name = 'Arirang TV World'
    default_action = 'play_stream' 

    def action_play_stream(self):
        self.plugin.set_stream_url('http://worldlive-ios.arirang.co.kr/arirang/arirangtvworldios.mp4.m3u8')
        
############
## Al Aan ##
############
        
#class AlAan(BaseChannel):
#    playable = True
#    short_name = 'alaan'
#    long_name = 'Al Aan'
#    default_action = 'play_stream'
#
#    def action_play_stream(self):
#        self.plugin.set_stream_url('http://alaan_hls-lh.akamaihd.net/i/alaan_ar@103399/master.m3u8')

##############
## Antena 3 ##
##############

class Antena3(BaseChannel):
    playable = True
    short_name = 'antena3'
    long_name = 'Antena 3'
    default_action = 'play_stream'

    def action_play_stream(self):
        self.plugin.set_stream_url('rtmp://93.115.84.226:1935/live playpath=a3 swfUrl=http://static.ls-cdn.com/player/5.10/livestation-player.swf swfVfy=1 live=1')

#############
## Al Alam ##
#############

#class AlAlam(BaseChannel):
#    playable = False
#    short_name = 'alalam'
#    long_name = 'Al Alam'
#    default_action = 'list_streams'
#    
#    def action_list_streams(self):
#        data = {}
#        data.update(self.args)
#	data.update({'action': 'play_stream', 'Title': 'High Quality', 'stream_url': 'rtmp://hd6.lsops.net/live/ playpath=alalam_ar_1428 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
#        self.plugin.add_list_item(data, is_folder=False)
#        data.update({'action': 'play_stream', 'Title': 'Medium Quality', 'stream_url': 'rtmp://hd6.lsops.net/live playpath=alalam_ar_584 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
#        self.plugin.add_list_item(data, is_folder=False)
#        data.update({'action': 'play_stream', 'Title': 'Low Quality', 'stream_url': 'rtmp://hd6.lsops.net/live playpath=alalam_ar_162 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
#        self.plugin.add_list_item(data, is_folder=False)
#        data.update({'action': 'play_stream', 'Title': 'Mobile Quality', 'stream_url': 'http://hd6.lsops.net/live/alalam_ar_hls.smil/playlist.m3u8'})
#        self.plugin.add_list_item(data, is_folder=False)
#        self.plugin.end_list()
#
#    def action_play_stream(self):        
#        self.plugin.set_stream_url(self.args['stream_url'])

##################
## AlJazeera AR ##
##################

class AlJazeeraArabic(BaseChannel):
    playable = False
    short_name = 'aljazeera_ar'
    long_name = 'Al Jazeera Arabic'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
	data.update({'action': 'play_stream', 'Title': 'High Quality', 'stream_url': 'rtmp://aljazeeraflashlivefs.fplive.net/aljazeeraflashlive-live/ playpath=aljazeera_ara_high swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Medium Quality', 'stream_url': 'rtmp://aljazeeraflashlivefs.fplive.net/aljazeeraflashlive-live/ playpath=aljazeera_ara_med swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Low Quality', 'stream_url': 'rtmp://aljazeeraflashlivefs.fplive.net/aljazeeraflashlive-live/ playpath=aljazeera_ara_low swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        #data.update({'action': 'play_stream', 'Title': 'Mobile Quality', 'stream_url': 'http://hd3.lsops.net/live/aljazeer_ar_hls.smil/playlist.m3u8'})
        #self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

##################
## AlJazeera EN ##
##################

class AlJazeeraEnglish(BaseChannel):
    playable = False
    short_name = 'aljazeera_en'
    long_name = 'Al Jazeera English'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
	data.update({'action': 'play_stream', 'Title': 'High Quality', 'stream_url': 'rtmp://aljazeeraflashlivefs.fplive.net/aljazeeraflashlive-live/ playpath=aljazeera_eng_high swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Medium Quality', 'stream_url': 'rtmp://aljazeeraflashlivefs.fplive.net/aljazeeraflashlive-live/ playpath=aljazeera_eng_med swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Low Quality', 'stream_url': 'rtmp://aljazeeraflashlivefs.fplive.net/aljazeeraflashlive-live/ playpath=aljazeera_eng_low swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        #data.update({'action': 'play_stream', 'Title': 'Mobile Quality', 'stream_url': 'http://hd2.lsops.net/live/aljazeer_en_hls.smil/playlist.m3u8'})
        #self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

##################
## AlJazeera US ##
##################

#class AlJazeeraAmerica(BaseChannel):
#    playable = False
#    short_name = 'aljazeera_us'
#    long_name = 'Al Jazeera America'
#    default_action = 'list_streams'
    
#    def action_list_streams(self):
#        data = {}
#        data.update(self.args)
#	data.update({'action': 'play_stream', 'Title': 'High Quality', 'stream_url': 'rtmp://ajam.lsops.net/live/ playpath=ajam_en_584 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
#        self.plugin.add_list_item(data, is_folder=False)
#        data.update({'action': 'play_stream', 'Title': 'Medium Quality', 'stream_url': 'rtmp://ajam.lsops.net/live/ playpath=ajam_en_364 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
#        self.plugin.add_list_item(data, is_folder=False)
#        data.update({'action': 'play_stream', 'Title': 'Low Quality', 'stream_url': 'rtmp://ajam.lsops.net/live/ playpath=ajam_en_162 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
#        self.plugin.add_list_item(data, is_folder=False)
#        data.update({'action': 'play_stream', 'Title': 'Mobile Quality', 'stream_url': 'http://ajam.lsops.net/live/ajam_en_hls.smil/playlist.m3u8'})
#        self.plugin.add_list_item(data, is_folder=False)
#        self.plugin.end_list()

#    def action_play_stream(self):        
#        self.plugin.set_stream_url(self.args['stream_url'])
        
#################
## Al Mayadeen ##
#################

#class VoAPersian(BaseChannel):
#    playable = False
#    short_name = 'almayadeen'
#    long_name = 'Al Mayadeen'
#    default_action = 'list_streams'
#    
#    def action_list_streams(self):
#        data = {}
#        data.update(self.args)
#        data.update({'action': 'play_stream', 'Title': 'Medium Quality', 'stream_url': 'rtmp://hd2.lsops.net/live playpath=almayade_ar_485 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
#        self.plugin.add_list_item(data, is_folder=False)
#        data.update({'action': 'play_stream', 'Title': 'Low Quality', 'stream_url': 'rtmp://hd2.lsops.net/live playpath=almayade_ar_183 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
#        self.plugin.add_list_item(data, is_folder=False)
#        data.update({'action': 'play_stream', 'Title': 'Mobile Quality', 'stream_url': 'http://hd2.lsops.net/live/almayade_ar_hls.smil/playlist.m3u8'})
#        self.plugin.add_list_item(data, is_folder=False)
#        self.plugin.end_list()
#
#    def action_play_stream(self):        
#        self.plugin.set_stream_url(self.args['stream_url'])
        
#################
## Al Nabaa TV ##
#################

#class VoAPersian(BaseChannel):
#    playable = False
#    short_name = 'alnabaa'
#    long_name = 'Al Nabaa TV'
#    default_action = 'list_streams'
#    
#    def action_list_streams(self):
#        data = {}
#        data.update(self.args)
#        data.update({'action': 'play_stream', 'Title': 'Standard Quality', 'stream_url': 'rtmp://alnabaa.lsops.net/live/ playpath=alnabaa_ar_584 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
#        self.plugin.add_list_item(data, is_folder=False)
#        data.update({'action': 'play_stream', 'Title': 'Medium Quality', 'stream_url': 'rtmp://alnabaa.lsops.net/live/ playpath=alnabaa_ar_364 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
#        self.plugin.add_list_item(data, is_folder=False)
#        data.update({'action': 'play_stream', 'Title': 'Low Quality', 'stream_url': 'rtmp://alnabaa.lsops.net/live/ playpath=alnabaa_ar_162 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
#        self.plugin.add_list_item(data, is_folder=False)
#        data.update({'action': 'play_stream', 'Title': 'Mobile Quality', 'stream_url': 'http://alnabaa.lsops.net/live/alnabaa_ar_hls.smil/playlist.m3u8'})
#        self.plugin.add_list_item(data, is_folder=False)
#        self.plugin.end_list()
#
#    def action_play_stream(self):        
#        self.plugin.set_stream_url(self.args['stream_url'])

##############
## ABC News ##
##############
        
class ABCNEWS(BaseChannel):
    playable = True
    short_name = 'abcnews'
    long_name = 'ABC News'
    default_action = 'play_stream'

    def action_play_stream(self):
        self.plugin.set_stream_url('http://abclive.abcnews.com/i/abc_live4@136330/master.m3u8?b=500,300,700,900,1200')

###############
## ABCNews24 ##
###############  

class ABCNews24(BaseChannel):
    playable = False
    short_name = 'abc24'
    long_name = 'ABC News 24'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
	data.update({'action': 'play_stream', 'Title': 'ABC News 24 - (Australia Only)', 'stream_url': 'http://www.abc.net.au/res/streaming/video/hls/news24.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'ABC News 24', 'stream_url': 'rtmp://cp103653.live.edgefcs.net:1935/live?_fcs_vhost=cp103653.live.edgefcs.net&akmfv=1.8 playpath=international_medium@36382 swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

#########
## BBC ##
#########  

class BBCNEWS(BaseChannel):
    playable = False
    short_name = 'bbc'
    long_name = 'BBC'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
	data.update({'action': 'play_stream', 'Title': 'BBC World', 'stream_url': 'http://c004.p105.edgesuite.net/i/c004/bbcworld_1@97498/master.m3u8'})
	self.plugin.add_list_item(data, is_folder=False)
	data.update({'action': 'play_stream', 'Title': 'BBC Arabic', 'stream_url': 'http://wpc.C1A9.edgecastcdn.net/hls-live/20C1A9/bbc_ar/ls_satlink/b_,264,528,828,.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'BBC Persian', 'stream_url': 'http://wpc.C1A9.edgecastcdn.net/hls-live/20C1A9/bbc_persian/ls_satlink/b_,264,528,828,.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])


##########
## CNBC ##
##########

class CNBC(BaseChannel):
    playable = True
    short_name = 'cnbc'
    long_name = 'CNBC'
    default_action = 'play_stream' 

    def action_play_stream(self):
        self.plugin.set_stream_url('http://origin2.live.web.tv.streamprovider.net/streams/3bc166ba3776c04e987eb242710e75c0/index.m3u8')

########
## RT ##
########
        
class RT(BaseChannel):
    playable = False
    short_name = 'rt'
    long_name = 'RT'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'Global', 'stream_url': 'http://rt-a.akamaihd.net/ch_01@325605/master.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Spanish', 'stream_url': 'http://rt-a.akamaihd.net/ch_02@325606/master.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Arabic', 'stream_url': 'http://rt-a.akamaihd.net/ch_03@325607/master.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'America', 'stream_url': 'http://rt-a.akamaihd.net/ch_04@325608/master.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'UK', 'stream_url': '"http://rt-a.akamaihd.net/ch_06@325610/master.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Documentaries', 'stream_url': 'http://rt-a.akamaihd.net/ch_05@325609/master.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

#############
## i24news ##
#############
        
class i24news(BaseChannel):
    playable = False
    short_name = 'i24news'
    long_name = 'i24news'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'English', 'stream_url': 'http://bcoveliveios-i.akamaihd.net/hls/live/215102/master_english/398/master.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'French', 'stream_url': 'http://bcoveliveios-i.akamaihd.net/hls/live/215102/master_french/412/master.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Arabic', 'stream_url': 'http://bcoveliveios-i.akamaihd.net/hls/live/215102/master_arabic/391/master.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])
    
##############
## EuroNews ##
##############

class EuroNews(BaseChannel):
    playable = False
    short_name = 'euronews'
    long_name = 'EuroNews'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'Arabic', 'stream_url': 'rtsp://ewns-hls-b-stream.hexaglobe.net/rtpeuronewslive/ar_vidan750_rtp.sdp'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'English', 'stream_url': 'rtsp://ewns-hls-b-stream.hexaglobe.net/rtpeuronewslive/en_vidan750_rtp.sdp'})
        self.plugin.add_list_item(data, is_folder=False)
	data.update({'action': 'play_stream', 'Title': 'French', 'stream_url': 'rtsp://ewns-hls-b-stream.hexaglobe.net/rtpeuronewslive/fr_vidan750_rtp.sdp'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'German', 'stream_url': 'rtsp://ewns-hls-b-stream.hexaglobe.net/rtpeuronewslive/de_vidan750_rtp.sdp'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Italian', 'stream_url': 'rtsp://ewns-hls-b-stream.hexaglobe.net/rtpeuronewslive/it_vidan750_rtp.sdp'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Portuguese', 'stream_url': 'rtsp://ewns-hls-b-stream.hexaglobe.net/rtpeuronewslive/pt_vidan750_rtp.sdp'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Russian', 'stream_url': 'rtsp://ewns-hls-b-stream.hexaglobe.net/rtpeuronewslive/ru_vidan750_rtp.sdp'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Spanish', 'stream_url': 'rtsp://ewns-hls-b-stream.hexaglobe.net/rtpeuronewslive/es_vidan750_rtp.sdp'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Turkish', 'stream_url': 'rtsp://ewns-hls-b-stream.hexaglobe.net/rtpeuronewslive/tr_vidan750_rtp.sdp'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

#############
## NASA TV ##
#############

class NASATV(BaseChannel):
    playable = False
    short_name = 'nasatv_en'
    long_name = 'NASA TV'
    default_action = 'list_streams'
	
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'NASA TV', 'stream_url': 'rtmp://infozen.fc.llnwd.net/infozen/ playpath=nasa_400 swfUrl=http://static.ls-cdn.com/player/5.10/livestation-player.swf swfVfy=1 live=1'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'NASA TV HD', 'stream_url': 'rtmp://infozen.fc.llnwd.net/infozen/ playpath=nasa_1000 swfUrl=http://static.ls-cdn.com/player/5.10/livestation-player.swf swfVfy=1 live=1'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'NASA Public Channel', 'stream_url': 'rtmp://ustreamlivefs.fplive.net/ustream2live-live/ playpath=stream_live_1_1_6540154 swfUrl=http://static-cdn1.ustream.tv/swf/live/viewer.rsl:96.swf swfVfy=1 live=1'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'NASA Media Channel', 'stream_url': 'rtmp://ustreamlivefs.fplive.net/ustream4live-live/ playpath=stream_live_1_1_10414700 swfUrl=http://static-cdn1.ustream.tv/swf/live/viewer.rsl:96.swf swfVfy=1 live=1'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'NASA Education Channel', 'stream_url': 'rtmp://infozen.fc.llnwd.net/infozen/edu_channel.flv'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'NASA Space Station Live', 'stream_url': 'rtmp://ustreamlivefs.fplive.net/ustream3live-live/ playpath=stream_live_1_1_9408562 swfUrl=http://static-cdn1.ustream.tv/swf/live/viewer.rsl:96.swf swfVfy=1 live=1'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

#############
## Reuters ##
#############	

class REUTERS(BaseChannel):
    playable = True
    short_name = 'reuters'
    long_name = 'Reuters'
    default_action = 'play_stream'
    
    def action_play_stream(self):
	self.plugin.set_stream_url('http://37.58.85.156/rlo001/ngrp:rlo001.stream_all/playlist.m3u8')


################
## Rai News24 ##
################

class RAINEWS24(BaseChannel):
    playable = False
    short_name = 'rainews24'
    long_name = 'Rai News24 (Geo-restricted)'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'Medium Quality', 'stream_url': 'rtmp://rainews.lsops.net/live/ playpath=rainews_it_584 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Mobile Quality', 'stream_url': 'http://rainews.lsops.net/live/rainews_it_hls.smil/playlist.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

#############
## PressTV ##
#############	

class PRESSTV(BaseChannel):
    playable = True
    short_name = 'press_tv'
    long_name = 'PressTV'
    default_action = 'play_stream'
    
    def action_play_stream(self):
	self.plugin.set_stream_url('rtmp://mtv.fms-01.visionip.tv/live/&file=mtv-ptv-live-25f-16x9-SDh&type=rtmp&rtmp.subscribe=true&autostart=true&stretching=exactfit')

###############
## Bloomberg ##
###############

class BLOOMBERG(BaseChannel):
    playable = True
    short_name = 'bloomberg_en'
    long_name = 'Bloomberg Television'
    default_action = 'play_stream'
    
    def action_play_stream(self):        
        self.plugin.set_stream_url('http://live.bltvios.com.edgesuite.net/tv/us/master.m3u8')

####################################
## Channel NewsAsia International ##
####################################

class CNAI(BaseChannel):
    playable=True
    short_name = 'channel_newsasia'
    long_name = "Channel NewsAsia International (Geo-restricted)"
    default_action = 'play_stream'

    def action_play_stream(self):        
        self.plugin.set_stream_url('http://cna_hls-lh.akamaihd.net/i/cna_en@8000/master.m3u8')
	
##########
## eNCA ##
##########

class eNCA(BaseChannel):
    playable=True
    short_name = 'enca'
    long_name = "eNCA (South Africa)"
    default_action = 'play_stream'

    def action_play_stream(self):        
        self.plugin.set_stream_url('http://wpc.C1A9.edgecastcdn.net/hls-live/20C1A9/enca/ls_satlink/b_,264,528,828,.m3u8')

##############
## Sky News ##
##############

class SkyNews(BaseChannel):
    playable = False
    short_name = 'skynews'
    long_name = 'Sky News'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'Sky News', 'stream_url': 'http://ilg.club/streamlink.m3u8?channel_id=31b003ab7e7749a798fe00424e3dd9ff&bitrate=800'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Sky News Live HD', 'stream_url': 'plugin://plugin.video.youtube/?action=play_video&videoid=mqafQVNkyN4'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Sky News International', 'stream_url': 'http://wpc.C1A9.edgecastcdn.net/hls-live/20C1A9/skynews/ls_satlink/b_,264,528,828,.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Sky News Arabia', 'stream_url': 'http://hd7.lsops.net/live/skynewsi_ar_hls.smil/playlist.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

##############
## France24 ##
##############

class France24(BaseChannel):
    playable = False
    short_name = 'france24'
    long_name = 'France 24'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'English', 'stream_url': 'http://static.france24.com/live/F24_EN_LO_HLS/live_ios.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'French', 'stream_url': 'http://static.france24.com/live/F24_FR_LO_HLS/live_ios.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])
    
####################
## Deutsche Welle ##
####################    

class DW(BaseChannel):
    playable = False
    short_name = 'dw'
    long_name = 'Deutsche Welle (DW)'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'DW', 'stream_url': 'http://www.metafilegenerator.de/DWelle/tv/ios/master.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'DW (North America)', 'stream_url': 'http://www.metafilegenerator.de/DWelle/tv-northamerica/ios/master.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'DW (Arabia)', 'stream_url': 'http://www.metafilegenerator.de/DWelle/tv-arabia/ios/master.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'DW (Asia)', 'stream_url': 'http://www.metafilegenerator.de/DWelle/tv-asia/ios/master.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'DW (Europe)', 'stream_url': 'http://www.metafilegenerator.de/DWelle/tv-europa/ios/master.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'DW (Latinoamerica)', 'stream_url': 'http://www.metafilegenerator.de/DWelle/tv-latinoamerica/ios/master.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])
        
#################
## VoA Persian ##
#################

class VoAPersian(BaseChannel):
    playable = False
    short_name = 'voapersian'
    long_name = 'VoA Persian'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data.update({'action': 'play_stream', 'Title': 'Medium Quality', 'stream_url': 'rtmp://hd4.lsops.net/live playpath=voiceofa_fa_485 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Low Quality', 'stream_url': 'rtmp://hd4.lsops.net/live playpath=voiceofa_fa_183 swfUrl="http://static.ls-cdn.com/player/5.10/livestation-player.swf" swfVfy=true live=true'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'action': 'play_stream', 'Title': 'Mobile Quality', 'stream_url': 'http://hd4.lsops.net/live/voiceofa_fa_hls.smil/playlist.m3u8'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

########################
## The People's Voice ##
########################    

#class TPV(BaseChannel):
#    playable = False
#    short_name = 'tpv'
#    long_name = 'The People`s Voice'
#    default_action = 'list_streams'
#    
#    def action_list_streams(self):
#        data = {}
#        data.update(self.args)
#        data.update({'action': 'play_stream', 'Title': 'High Quality', 'stream_url': 'rtmp://cdn.rbm.tv/rightbrainmedia-live-106/_definst_/ddstream_3'})
#        self.plugin.add_list_item(data, is_folder=False)
#        data.update({'action': 'play_stream', 'Title': 'Mobile Quality', 'stream_url': 'http://cdn.rbm.tv:1935/rightbrainmedia-live-106/_definst_/ddstream_3/playlist.m3u8'})
#        self.plugin.add_list_item(data, is_folder=False)
#        self.plugin.end_list()
#
#    def action_play_stream(self):        
#        self.plugin.set_stream_url(self.args['stream_url'])
        
###############
## NHK WORLD ##
###############

#class NHK(BaseChannel):
#    playable = True
#    short_name = 'nhk_world'
#    long_name = 'NHK World TV'
#    default_action = 'play_stream' 
#
#    def action_play_stream(self):
#        self.plugin.set_stream_url('http://plslive-w.nhk.or.jp/nhkworld/app/live.m3u8')
        
###############
## CCTV News ##
###############

class CCTV(BaseChannel):
    playable = True
    short_name = 'cctv_news_english'
    long_name = 'CCTV News'
    default_action = 'play_stream' 

    def action_play_stream(self):
        self.plugin.set_stream_url('http://origin2.live.web.tv.streamprovider.net/streams/877ba7a57aa68fd898b838f58d51a69f/index.m3u8')   

###################
## MHz Worldview ##
###################

class MHz(BaseChannel):
    playable = True
    short_name = 'mhz_worldview'
    long_name = 'MHz Worldview'
    default_action = 'play_stream' 

    def action_play_stream(self):
        self.plugin.set_stream_url('rtmp://tvrtmp2.tulix.tv:1935/mhztna/mhztna2 swfUrl=http://swf.tulix.tv/jwplayer/jwplayer.flash.swf live=1 pageUrl=http://www.tulix.com/iframe/mhzabr/index.php')
        
#########
## CNN ##
#########

class CNN(BaseChannel):
    playable = False
    short_name = 'cnn'
    long_name = 'CNN International'
    default_action = 'list_streams'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data['action'] = 'play_stream'
        data.update({'stream_url': "http://wpc.c1a9.edgecastcdn.net/hls-live/20C1A9/cnn/ls_satlink/b_528.m3u8", 'Title': 'Medium Quality'})
        self.plugin.add_list_item(data, is_folder=False)
	#data.update({'stream_url': "rtmp://c.cdn.livenewschat.eu/edge/ playpath=cnn_live swfUrl='http://msnbclive.eu/player.swf' swfVfy=true live=true", 'Title': 'CNN UK'})
        #self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()

    def action_play_stream(self):        
        self.plugin.set_stream_url(self.args['stream_url'])

##############
## 24 Vesti ##
##############

class VESTI(BaseChannel):
    playable = True
    short_name = '24vesti'
    long_name = '24 Vesti'
    default_action = 'play_stream'
    
    def action_play_stream(self):
	self.plugin.set_stream_url('mms://62.162.58.55/24vesti')
	
###############
## NDTV 24x7 ##
###############

class NDTV(BaseChannel):
    playable = True
    short_name = 'ndtv_24x7'
    long_name = 'NDTV 24x7'
    default_action = 'play_stream' 

    def action_play_stream(self):
        self.plugin.set_stream_url('http://bglive-a.bitgravity.com/ndtv/247hi/live/native')
        
###################
## tagessschau24 ##
###################

class Tagesschau24(BaseChannel):
    playable = True
    short_name = 'tagesschau24'
    long_name = 'tagesschau24'
    default_action = 'play_stream' 

    def action_play_stream(self):
        self.plugin.set_stream_url('http://tagesschau-lh.akamaihd.net/i/tagesschau_1@119231/master.m3u8')
    
###########
## CSpan ##
###########

class CSpan(BaseChannel):
    playable = False
    short_name = 'cspan_en'
    long_name = 'CSPAN'
    default_action = 'list_streams'
    swf_url = 'http://www.c-span.org/cspanVideoHD.swf'
    
    def action_list_streams(self):
        data = {}
        data.update(self.args)
        data['action'] = 'play_stream'
        data.update({'stream_url': "rtmp://cp82346.live.edgefcs.net/live/CSPAN1@14845", 'Title': 'CSPAN1'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'stream_url': "rtmp://cp82347.live.edgefcs.net/live/CSPAN2@14846", 'Title': 'CSPAN2'})
        self.plugin.add_list_item(data, is_folder=False)
        data.update({'stream_url': "rtmp://cp82348.live.edgefcs.net/live/CSPAN3@14847", 'Title': 'CSPAN3'})
        self.plugin.add_list_item(data, is_folder=False)
        self.plugin.end_list()
        
        
    def action_play_stream(self):
        parser = URLParser(swf_url = self.swf_url)
        self.plugin.set_stream_url(parser(self.args['stream_url']))          


#############
## Digi 24 ##
#############

class Digi24(BaseChannel):
    playable = True
    short_name = 'digi24'
    long_name = 'Digi 24'
    default_action = 'play_stream' 

    def action_play_stream(self):
        self.plugin.set_stream_url('http://82.76.249.77:80/digi24edge/digi24hdhqhls/index.m3u8')
