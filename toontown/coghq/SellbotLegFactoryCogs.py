from SpecImports import *
import random
LobbyParent = 10014
BoilerParent = 10030
PipeLeftParent = 10023
PipeRightParent = 10032
OilParent = 10034
ControlParent = 10037
DuctParent = 10036
CenterSiloBattleCellParent = 10064
CenterSiloParent = 20095
SigRoomParent = 20058
WestSiloParent = 20094
WestSiloBattleCellParent = 10047
EastSiloParent = 20096
EastSiloBattleCellParent = 10068
LobbyCell = 0
BoilerCell = 1
PipeLeftCell = 2
PipeRightCell = 3
OilCell = 4
ControlCell = 5
DuctCell = 6
CenterSiloCell = 7
SigRoomCell = 8
WestSiloCell = 9
EastSiloCell = 10
BattleCells = {LobbyCell: {'parentEntId': LobbyParent,
             'pos': Point3(0, 0, 0)},
 BoilerCell: {'parentEntId': BoilerParent,
              'pos': Point3(0, 0, 0)},
 OilCell: {'parentEntId': OilParent,
           'pos': Point3(0, 0, 0)},
 ControlCell: {'parentEntId': ControlParent,
               'pos': Point3(0, 0, 0)},
 CenterSiloCell: {'parentEntId': CenterSiloBattleCellParent,
                  'pos': Point3(0, 0, 0)},
 PipeLeftCell: {'parentEntId': PipeLeftParent,
                'pos': Point3(0, 0, 0)},
 PipeRightCell: {'parentEntId': PipeRightParent,
                 'pos': Point3(0, 0, 0)},
 DuctCell: {'parentEntId': DuctParent,
            'pos': Point3(0, 0, 0)},
 SigRoomCell: {'parentEntId': SigRoomParent,
               'pos': Point3(0, 0, 0)},
 WestSiloCell: {'parentEntId': WestSiloBattleCellParent,
                'pos': Point3(0, 0, 0)},
 EastSiloCell: {'parentEntId': EastSiloBattleCellParent,
                'pos': Point3(-20, -10, 0)}}
CogData = [{'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': LobbyParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
  'battleCell': LobbyCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20078,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': LobbyParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
  'battleCell': LobbyCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20009,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': LobbyParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': LobbyCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20079,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': BoilerParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': BoilerCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'walk',
  'path': 20076,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': BoilerParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': BoilerCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'walk',
  'path': 20077,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': BoilerParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': BoilerCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': OilParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': OilCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 60133,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': OilParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': OilCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 60134,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': OilParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': OilCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 60135,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': ControlParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': ControlCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20039,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': ControlParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': ControlCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20049,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': ControlParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': ControlCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20075,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': CenterSiloCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20103,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['mh']),
  'parentEntId': CenterSiloParent,
  'boss': 1,
  'level': random.choice([11, 12, 13]),
  'battleCell': CenterSiloCell,
  'pos': Point3(0, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': CenterSiloCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20104,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': CenterSiloCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20105,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': WestSiloParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': WestSiloCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20097,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': WestSiloParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': WestSiloCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20098,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': WestSiloParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': WestSiloCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20099,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': EastSiloParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': EastSiloCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20100,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': EastSiloParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': EastSiloCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20101,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': EastSiloParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': EastSiloCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20102,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': PipeLeftParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': PipeLeftCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20109,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': PipeLeftParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': PipeLeftCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20110,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': PipeLeftParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': PipeLeftCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20111,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': PipeRightParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': PipeRightCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20106,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': PipeRightParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': PipeRightCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20107,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': PipeRightParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': PipeRightCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20108,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': DuctParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': DuctCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20038,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': DuctParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': DuctCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20067,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': DuctParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': DuctCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20068,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': SigRoomParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': SigRoomCell,
  'pos': Point3(5, -10.75, 0),
  'h': -90,
  'behavior': 'stand',
  'path': None,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': SigRoomParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': SigRoomCell,
  'pos': Point3(5, -3.25, 0),
  'h': -90,
  'behavior': 'stand',
  'path': None,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': SigRoomParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': SigRoomCell,
  'pos': Point3(5, 3.25, 0),
  'h': -90,
  'behavior': 'stand',
  'path': None,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': SigRoomParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': SigRoomCell,
  'pos': Point3(5, 10.75, 0),
  'h': -90,
  'behavior': 'stand',
  'path': None,
  'skeleton': random.choice([0, 1])}]
ReserveCogData = [{'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': LobbyParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': LobbyCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20009,
  'skeleton': random.choice([0, 1]),
  'joinParent': 20018},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': BoilerParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': BoilerCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'walk',
  'path': 20076,
  'skeleton': random.choice([0, 1]),
  'joinParent': 20019},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']), 
  'parentEntId': BoilerParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': BoilerCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'walk',
  'path': 20077,
  'skeleton':  random.choice([0, 1]),
  'joinParent': 20019},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': OilParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': OilCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 60133,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': OilParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': OilCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 60135,
  'skeleton': random.choice([0, 1])},
 {'type':  random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': ControlParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': ControlCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20039,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': ControlParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': ControlCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20049,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': ControlParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': ControlCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'walk',
  'path': 20075,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': CenterSiloCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20103,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': CenterSiloCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': CenterSiloCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20104,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': CenterSiloParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': CenterSiloCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20105,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': PipeLeftParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': PipeLeftCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': PipeLeftParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': PipeLeftCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': PipeRightParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': PipeRightCell,
  'pos': Point3(-10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': PipeRightParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': PipeRightCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': None,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': DuctParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': DuctCell,
  'pos': Point3(0, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20038,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': DuctParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': DuctCell,
  'pos': Point3(10, 0, 0),
  'h': 0,
  'behavior': 'chase',
  'path': 20067,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']),
  'parentEntId': SigRoomParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': SigRoomCell,
  'pos': Point3(5, -10.75, 0),
  'h': -90,
  'behavior': 'stand',
  'path': None,
  'skeleton': random.choice([0, 1])},
 {'type': random.choice(['cc', 'tm', 'nd', 'gh', 'ms', 'tf', 'm', 'mh, pm']), 
  'parentEntId': SigRoomParent,
  'boss': 0,
  'level': random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]),
  'battleCell': SigRoomCell,
  'pos': Point3(5, -3.25, 0),
  'h': -90,
  'behavior': 'stand',
  'path': None,
  'skeleton': random.choice([0, 1])}]
