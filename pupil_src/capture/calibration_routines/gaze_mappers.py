'''
(*)~----------------------------------------------------------------------------------
 Pupil - eye tracking platform
 Copyright (C) 2012-2014  Pupil Labs

 Distributed under the terms of the CC BY-NC-SA License.
 License details are in the file license.txt, distributed as part of this software.
----------------------------------------------------------------------------------~(*)
'''

from plugin import Gaze_Mapping_Plugin

class Dummy_Gaze_Mapper(Gaze_Mapping_Plugin):
    """docstring for Dummy_Gaze_Mapper"""
    def __init__(self, g_pool):
        super(Dummy_Gaze_Mapper, self).__init__(g_pool)

    def update(self,frame,recent_pupil_positions,events):
        gaze_pts = []

        for p in recent_pupil_positions:
            if p['confidence'] > self.g_pool.pupil_confidece_threshold:
                gaze_pts.append({'norm_pos':p['norm_pos'][:],'confidence':p['confidence'],'timestamp':p['timestamp']})

        events['gaze'] = gaze_pts


    def get_init_dict(self):
        return {}


class Simple_Gaze_Mapper(Gaze_Mapping_Plugin):
    """docstring for Simple_Gaze_Mapper"""
    def __init__(self, g_pool,map_fn):
        super(Simple_Gaze_Mapper, self).__init__(g_pool)
        self.map_fn = map_fn


    def update(self,frame,recent_pupil_positions,events):
        gaze_pts = []

        for p in recent_pupil_positions:
            if p['confidence'] > self.g_pool.pupil_confidece_threshold:
                gaze_point = self.map_fn(p['norm_pos'])
                gaze_pts.append({'norm_pos':p['norm_pos'][:],'confidence':p['confidence'],'timestamp':p['timestamp']})

        events['gaze'] = gaze_pts

    def get_init_dict(self):
        return {'map_fn':self.map_fn}


class Volumetric_Gaze_Mapper(Gaze_Mapping_Plugin):
    def __init__(self, g_pool,params):
        super(Volumetric_Gaze_Mapper, self).__init__(g_pool)
        self.params = params


    def update(self,frame,recent_pupil_positions,events):
        gaze_pts = []
        raise NotImplementedError
        events['gaze'] = gaze_pts

    def get_init_dict(self):
        return {'params':self.params}

class Bilateral_Gaze_Mapper(Gaze_Mapping_Plugin):
    def __init__(self, g_pool,params):
        super(Volumetric_Gaze_Mapper, self).__init__(g_pool)
        self.params = params

    def update(self,frame,recent_pupil_positions,events):
        gaze_pts = []
        raise NotImplementedError
        events['gaze'] = gaze_pts

    def get_init_dict(self):
        return {'params':self.params}