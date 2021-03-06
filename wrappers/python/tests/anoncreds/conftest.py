import json

import pytest

from indy import anoncreds
from tests.conftest import path_home as x_path_home, credentials as x_credentials, \
    wallet_handle_cleanup as x_wallet_handle_cleanup, wallet_handle as x_wallet_handle, xwallet as x_xwallet


@pytest.fixture(scope="session")
def path_home():
    # noinspection PyTypeChecker
    for i in x_path_home():
        yield i


@pytest.fixture(scope="session")
def wallet_config():
    return '{"id":"anoncreds_common_wallet"}'


@pytest.fixture(scope="session")
def credential():
    return x_credentials()


@pytest.fixture(scope="session")
def xwallet_cleanup():
    return False


# noinspection PyUnusedLocal
@pytest.fixture(scope="session")

def xwallet(event_loop, xwallet_cleanup, path_home, wallet_config, credential):
    xwallet_gen = x_xwallet(event_loop, xwallet_cleanup, path_home, wallet_config, credential)
    yield next(xwallet_gen)
    next(xwallet_gen)


@pytest.fixture(scope="session")
def wallet_handle_cleanup():
    return x_wallet_handle_cleanup()


@pytest.fixture(scope="session")
def wallet_handle(event_loop, xwallet, wallet_config, credential, wallet_handle_cleanup):
    wallet_handle_gen = \
        x_wallet_handle(event_loop, xwallet, wallet_config, credential, wallet_handle_cleanup)
    yield next(wallet_handle_gen)
    next(wallet_handle_gen)


@pytest.fixture(scope="session")
def default_cred_def_config():
    return json.dumps({"support_revocation": False})


@pytest.fixture(scope="session")
def tag():
    return "tag1"


@pytest.fixture(scope="session")
def id_credential_1():
    return "id_credential_1"


@pytest.fixture(scope="session")
def id_credential_2():
    return "id_credential_2"


@pytest.fixture(scope="session")
def id_credential_3():
    return "id_credential_3"


@pytest.fixture(scope="session")
def id_credential_x():
    return "id_credential_x"


@pytest.fixture(scope="session")
def issuer_did():
    return "NcYxiDXkpYi6ov5FcYDi1e"


@pytest.fixture(scope="session")
def issuer_did_2():
    return "VsKV7grR1BUE29mG2Fm2kX"


@pytest.fixture(scope="session")
def prover_did():
    return "CnEDk9HrMnmiHXEV1WFgbVCRteYnPqsJwrTdcZaNhFVW"


def build_id(identifier: str, marker: str, word1: str, word2: str, word3: str):
    delimiter = ":"
    return identifier + delimiter + marker + delimiter + word1 + delimiter + word2 + delimiter + word3


@pytest.fixture(scope="session")
async def gvt_schema_tuple(issuer_did):
    return await anoncreds.issuer_create_schema(issuer_did, "gvt", "1.0", json.dumps(["name", "age", "sex", "height"]))


@pytest.fixture(scope="session")
def gvt_schema_id(gvt_schema_tuple):
    (schema_id, _) = gvt_schema_tuple
    return schema_id


@pytest.fixture(scope="session")
def gvt_schema(gvt_schema_tuple):
    (_, schema_json) = gvt_schema_tuple
    return json.loads(schema_json)


@pytest.fixture(scope="session")
async def gvt_schema_json(gvt_schema_tuple):
    (_, schema_json) = gvt_schema_tuple
    return schema_json


@pytest.fixture(scope="session")
async def xyz_schema_tuple(issuer_did):
    return await anoncreds.issuer_create_schema(issuer_did, "xyz", "1.0", json.dumps(["status", "period"]))


@pytest.fixture(scope="session")
def xyz_schema_id(xyz_schema_tuple):
    (schema_id, _) = xyz_schema_tuple
    return schema_id


@pytest.fixture(scope="session")
def xyz_schema(xyz_schema_tuple):
    (_, schema_json) = xyz_schema_tuple
    return json.loads(schema_json)


@pytest.fixture(scope="session")
async def xyz_schema_json(xyz_schema_tuple):
    (_, schema_json) = xyz_schema_tuple
    return schema_json


@pytest.fixture(scope="session")
def master_secret_id():
    return "common_master_secret_name"


@pytest.fixture(scope="session")
def issuer_1_gvt_cred_def_id(issuer_did, gvt_schema_id, tag):
    return build_id(issuer_did, "3", "CL", gvt_schema_id, tag)


@pytest.fixture(scope="session")
def issuer_1_xyz_cred_def_id(issuer_did, xyz_schema_id, tag):
    return build_id(issuer_did, "3", "CL", xyz_schema_id, tag)


@pytest.fixture(scope="session")
def issuer_2_gvt_cred_def_id(issuer_did_2, gvt_schema_id, tag):
    return build_id(issuer_did_2, "3", "CL", gvt_schema_id, tag)


@pytest.fixture(scope="session")
def credential_offer(credential_def_id):
    return {
        "schema_id": "NcYxiDXkpYi6ov5FcYDi1e:2:gvt:1.0",
        "cred_def_id": "NcYxiDXkpYi6ov5FcYDi1e:3:CL:NcYxiDXkpYi6ov5FcYDi1e:2:gvt:1.0",
        "key_correctness_proof": {
            "c": "69162495710840664618738545454662900282010320128225044250053827275963402208577",
            "xz_cap": "1291626533077507475824085098196940020962044312247442052738283685245211739821919763798729470717119810966112520169291457850850482635603467422394418696458435983068927671531676071057162723538103962728334909628780757669039354430799646710759812610255490309369746402035992758025440611538725268465965826117825920901062702782586489009822867853436945496064274986403248574539845188333871806385973222804134088900635644849978014315455844134746038723173510682780096137780946233957793989422958664074874051490901235765076512765646850831830656216974382980265359516805196396339581093492498344885680665565572289264578392073452536245380420906345693099843424070668652986985600398173151708567520393541743867310438781",
            "xr_cap": [
                ["master_secret",
                 "1381727434322198801487662543132108214967952332690132157797744341733881186164821669929922604403793208643971236240281832859022377712216986871840871065282894339158046565473156546781247789638185265794584841290166221019032341312183202049311919861377024390914573999094125587631451605840947258435695064488145011477832348961814334781987834206637760421918194879125799291565487566331474567676881908995822496620501513947273752613726037244524497482510041574259199787793552722259136494215890493931200811893636477742618376316608715992027619354858556790788543262775526797589366729411461702741169594815375097741771437155184326142513364011722195939064684797365915230686530081381191120691229314893216093783102755"],
                ["sex",
                 "212620670563846912141499815614993331487201362302564326358814949790104778777646930481367139673255222181080961959248700567467036454161484147574701371805233593603603069985490312476890981082367374888328076756038380055431111100487553752815626297406804238192576285167144077413440235825806957294798669081126905177005132712821419637066858943862703086460508462281545229430791736627219719352098169619305889437372340600437088730411783998085856624673409855828829888766563710855377623171275196732739786214738310851315094117113371039907149504951085259992742127257324729546538089241023420899902920792440672541645963812250468607138897614973933058531156935526728892477862636486590291167121624940442902692790222"],
                ["height",
                 "829210963917376253743719347475516119833506654078827192929879223257533862127006621694185135063618389585029332138423173736133892402277497576716123778521886107573844738753881648082400186965565942808601300878256403800893363800901390667595573057372140564397963202468286456620197995691944664655936568967832679333923463701245005313758794954246976941498954807694163908297717130821183768105993680589354914770535926049069412362969774333234959915101148040630000364956854128862436640554837103489372924007030890166911176286639810821739783691688701759913242242255483575167123627726009784262546175305035267018027338467644752318541071264834429496244317736639283213399749366425233150009501364414220099373578004"],
                ["name",
                 "1474769243010979114449140341475263715472238893688670901053711386885446913512315680742185583090335387791535042619202715485431453990119160178587437084985468086901142655546519824448511326943003679814130825072784577228013044511661506027923335834125039009831159467395426706012502359414366928440037646314466804914420347367131692936010748426360871498183045739975811690423730316184475087279262608262693191942498370217954456045638497326044862591144271197642514270742015614406172093123604736643739804945873457191770990242273518401516557969664039800446769895892059690371663656476249095336574071359322653586720437239516903961251590413673856949990484238475983678702850293337084753546371289600637161197573986"],
                ["age",
                 "871118890483431899713612237746742678182995153863791663213656765029348148222906906194599815000086922947943034793604470200853712518653841498149833032879919071293283137184051610434053422969843871978177974542727618239567816972009973735009345974890110440194964471031679119690515734747129204773619744383411653633334157647869384441794289079882541390209315445912773571798707120197345597429638698218251686665166774644534475340055973106953398617674634692246376045794397738522654567142977528525329513405111620175824457267888412214258063240051380612902174950236985995207610900351568372888641866744778917492184204173849157376116701007689131286017573172664232760280721866096443023199559625029767860311852879"]
            ]
        },
        "nonce": "939118265088633088940604"
    }


@pytest.fixture(scope="session")
def issuer_1_gvt_cred_offer(issuer_1_gvt_cred_def_id):
    return credential_offer(issuer_1_gvt_cred_def_id)


@pytest.fixture(scope="session")
def issuer_1_gvt_cred_offer_json(credential_offer_issuer_1_schema_1):
    return json.dumps(credential_offer_issuer_1_schema_1)


@pytest.fixture(scope="session")
def issuer_1_xyz_cred_offer_json(issuer_1_xyz_cred_def_id):
    return credential_offer(issuer_1_xyz_cred_def_id)


@pytest.fixture(scope="session")
def issuer_1_xyz_cred_offer_json(credential_offer_issuer_1_schema_2):
    return json.dumps(credential_offer_issuer_1_schema_2)


@pytest.fixture(scope="session")
def issuer_2_gvt_cred_offer(issuer_2_gvt_cred_def_id):
    return credential_offer(issuer_2_gvt_cred_def_id)


@pytest.fixture(scope="session")
def issuer_2_gvt_cred_offer_json(credential_offer_issuer_2_schema_1):
    return json.dumps(credential_offer_issuer_2_schema_1)


@pytest.fixture(scope="session")
def gvt_cred_values():
    # note that encoding is not standardized by Indy except that 32-bit integers are encoded as themselves. IS-786
    return {
        "sex": {
            "raw": "male", "encoded": "5944657099558967239210949258394887428692050081607692519917050011144233115103"},
        "name": {"raw": "Alex", "encoded": "1139481716457488690172217916278103335"},
        "height": {"raw": "175", "encoded": "175"},
        "age": {"raw": "28", "encoded": "28"}
    }


@pytest.fixture(scope="session")
def gvt_cred_values_json(gvt_cred_values):
    return json.dumps(gvt_cred_values)


@pytest.fixture(scope="session")
def gvt_cred_values_2():
    return {
        "sex": {
            "raw": "male", "encoded": "2142657394558967239210949258394838228692050081607692519917028371144233115103"},
        "name": {"raw": "Alexander", "encoded": "21332817548165488690172217217278169335"},
        "height": {"raw": "170", "encoded": "170"},
        "age": {"raw": "28", "encoded": "28"}
    }


@pytest.fixture(scope="session")
def gvt_2_cred_values_json(gvt_cred_values_2):
    return json.dumps(gvt_cred_values_2)


@pytest.fixture(scope="session")
def xyz_cred_values():
    return {
        "status": {"raw": "partial", "encoded": "51792877103171595686471452153480627530895"},
        "period": {"raw": "8", "encoded": "8"}
    }


@pytest.fixture(scope="session")
def xyz_cred_values_json(xyz_cred_values):
    return json.dumps(xyz_cred_values)


@pytest.fixture(scope="session")
def predicate_value():
    return 18


@pytest.fixture(scope="session")
def proof_req(predicate_value):
    return {
        "nonce": "123432421212",
        "name": "proof_req_1",
        "version": "0.1",
        "requested_attributes": {
            "attr1_referent": {"name": "name"}
        },
        "requested_predicates": {
            "predicate1_referent": {
                "name": "age",
                "p_type": ">=",
                "p_value": predicate_value
            }
        }
    }


@pytest.fixture(scope="session")
def proof_req_json(proof_req):
    return json.dumps(proof_req)


@pytest.fixture(scope="session")
def credential_def(gvt_schema_id, issuer_1_gvt_cred_def_id):
    return {
        "ver": "1.0",
        "id": "NcYxiDXkpYi6ov5FcYDi1e:3:CL:NcYxiDXkpYi6ov5FcYDi1e:2:gvt:1.0",
        "schemaId": "NcYxiDXkpYi6ov5FcYDi1e:2:gvt:1.0",
        "type": "CL",
        "tag": "tag1",
        "value": {
            "primary": {
                "n": "93903016580960826211255394743084454322651989553406123311533131276065200212810759076604218115871865661991138486481979641169910081623147782173417280333748584247996243768923368075293530338432655546084762386000283550052101261260535480047021393860552323356227888433010103478776022351285499486522640321696997912070759450202488615706721268107917954160898221852967025649320538743052603453056005349648527570545633707581997280058299497469111250360668699431874816221078541280677728894771043427243735838838924154365886418170575144843596101238848317296554648650851530302364102010725387694653238478998963325197022514619786856035381",
                "s": "83676820319322258953693412672920525458348931369699300027245595478354588396341380043825797348062515988024232699350211947307879360771822088188117055745594230587305261739452667532698270431300888028925634041524424958657510251474289539702600639447625499360536993525540491895186087426508001753416324200711401451681030302648723042077266334768551217523481300850104277156305997610124882945650381062511273974847257026289497827364485356768266751015987589160779363623143720972223369340234503991302891129505293527654858954142499610616340646122723497904443642680461224285518065214565555722177937083432837405313523299534462356249176",
                "r": {
                    "name": "47495604943828310485400590337976817602250878537697639950984937903635208915769126861395093693326826813179760018271449892277297055053132945171634961443652070758401714574365115230877743854045319116810843192770504737063957752668138110397121494248426229648259028205931308318445146904164975996349413108869109566478236817585742981940492241742585094760781284064047703068665322772700137879280546076453384433749580962445826378645180450659229569813998450809163222665234160845933413209027701177343434160562160555021641742844927919029108275489191585674028486171896060231192773454732713375076841165817674245143099837656333585167467",
                    "age": "57260990651909552438324980744915208450007555647548075792702602252957373165120362398639436374993747578667338654555906218241622166327554187173882032270911291524019845038919166596832792308619153724322409843422779977068687590126091616719709220529790429749906958275642179170646581305581293532191414369001925204710891571279391276262393759695734980926459027803775582100479691592618382817826201836563002915265730545427708598579504270692688333603038911054913220703965705624475175826699901595404360093858326988830274678756843993127150015170164553338869614443795013770717197748003844352256421364773854033308082184125941878381581",
                    "master_secret": "81087076981127410131340969836155541558001731071872651453638484184220871172046442984322510919754791936061019748363546186343454601374603783186393864482915694593886014335496316643390829685723228392272182645548252800817222808732446757681407584957247490162034468353431868754471060570430014014091964507403831880686985974511425731942472927570082478298184713513497141410980811399574065056520441942498406153507049105355624045005168289925299470592186518760490238677471231165057196401922176689873830847424075197410004569808356657799938568672156345018990652769716430470493533068823000151419289905514325540026615945563437162492387",
                    "height": "12754607548717884645850877144505808735370833293327357753593449606289975476756454937664292662375185538747740431474517331628512501182966834930297524664496971312102790249272675063970218633349382983183092978769817226534998748385907564653033782275529915223027585655087365271303276425823311882767850421250550453613955371862301728352727755429204533306056806489607525809607292934241569284635663406065599560401659525228920339934487154094313423670456946811717166509819027311828065496280462567568727365747019678140930112536106812362073320192218135009202868455106521002058222688184183732541283282099055674408655955487532993663005",
                    "sex": "33156081511472830691065735167534637219271963948083860086043333390683830172939272145870673024060582540975440771127141142015577610316696461370913699035219399580941351846986074068917438994808383349103701363287124838994618336753643532341046937095272803561166426504120633521156529485374606866749378431623145974800734369164386492437274576066925908791135093881309411263399881783743000335598336904318482606871346339837328519455538791299152607491745086101785403229637169893052902807089892505550633778989340452011655341797515056376043255842892664768015210103386157854874360215558403304152542859723962423896312727487847204926717"
                },
                "rctxt": "72006910083435945254237180987108072662543856464959679317518610973689661649534402354652624781485829233504601493374577173253671598832026156239626868727629817898124513158663822469539424401497848805604135929245831972388318877586838589283916733278204266265676110602701502235730153060660397968013410186984863161139079578640721480735545173311477882980351711525534947803990078682767420165151871381920799023343111595033518097770981248941386834251124532171246817605434425095977261026809010522467274618785963206939285970621015703002229468965636845281780889838938767805553403259040337365101190192326352621262135174752947066198685",
                "z": "7094245738325916331048006549007657148723991749866146721878009595786199702154750349914376511117103327159529072080260818960887615703130652617402306577105026104541131757761722730235799857659912296659280334415106260022231718131675194716633341985153003444311863612289370448173889827272330906132823097340706874788661993080532475877068469123320368969974031926060047072672294312989599167797808111940433000252161664080069442896751569106991827934300902302545878994493469833857389094732348607789523735791626907335345430926218706542048941533802823051000313776942891765472275357316333748353708307732832200039732370061713588310442"
            }
        }
    }


@pytest.fixture(scope="session")
def credential_def_json(credential_def):
    return json.dumps(credential_def)


@pytest.fixture(scope="session")
async def prepopulated_wallet(wallet_handle, gvt_schema_json, xyz_schema_json, gvt_cred_values_json,
                              gvt_2_cred_values_json, xyz_cred_values_json, issuer_did, issuer_did_2, master_secret_id,
                              prover_did, tag, default_cred_def_config, id_credential_1, id_credential_2,
                              id_credential_3, id_credential_x):
    # Create GVT credential by Issuer1
    (issuer1_gvt_cred_deg_id, issuer1_gvt_credential_def_json) = \
        await anoncreds.issuer_create_and_store_credential_def(wallet_handle, issuer_did, gvt_schema_json, tag,
                                                               None, default_cred_def_config)

    # Create XYZ credential by Issuer1
    (issuer1_xyz_cred_deg_id, issuer1_xyz_credential_def_json) = \
        await anoncreds.issuer_create_and_store_credential_def(wallet_handle, issuer_did, xyz_schema_json, tag,
                                                               None, default_cred_def_config)

    # Create GVT credential by Issuer2
    (issuer2_gvt_cred_def_id, issuer2_gvt_credential_def_json) = \
        await anoncreds.issuer_create_and_store_credential_def(wallet_handle, issuer_did_2, gvt_schema_json, tag,
                                                               None, default_cred_def_config)

    issuer_1_gvt_credential_offer_json = \
        await anoncreds.issuer_create_credential_offer(wallet_handle, issuer1_gvt_cred_deg_id)
    issuer_1_xyz_credential_offer_json = \
        await anoncreds.issuer_create_credential_offer(wallet_handle, issuer1_xyz_cred_deg_id)
    issuer_2_gvt_credential_offer_json = \
        await anoncreds.issuer_create_credential_offer(wallet_handle, issuer2_gvt_cred_def_id)

    await anoncreds.prover_create_master_secret(wallet_handle, master_secret_id)

    (issuer_1_gvt_cred_req, issuer_1_gvt_cred_req_metadata) = \
        await anoncreds.prover_create_credential_req(wallet_handle, prover_did, issuer_1_gvt_credential_offer_json,
                                                     issuer1_gvt_credential_def_json, master_secret_id)

    (issuer_1_gvt_cred, _, _) = \
        await anoncreds.issuer_create_credential(wallet_handle, issuer_1_gvt_credential_offer_json,
                                                 issuer_1_gvt_cred_req, gvt_cred_values_json, None, None)

    await anoncreds.prover_store_credential(wallet_handle, id_credential_1, issuer_1_gvt_cred_req_metadata,
                                            issuer_1_gvt_cred, issuer1_gvt_credential_def_json, None)

    (issuer_1_xyz_cred_req, issuer_1_xyz_cred_req_metadata) = \
        await anoncreds.prover_create_credential_req(wallet_handle, prover_did, issuer_1_xyz_credential_offer_json,
                                                     issuer1_xyz_credential_def_json, master_secret_id)

    (issuer_1_xyz_cred, _, _) = \
        await anoncreds.issuer_create_credential(wallet_handle, issuer_1_xyz_credential_offer_json,
                                                 issuer_1_xyz_cred_req, xyz_cred_values_json, None, None)

    await anoncreds.prover_store_credential(wallet_handle, id_credential_2, issuer_1_xyz_cred_req_metadata,
                                            issuer_1_xyz_cred, issuer1_xyz_credential_def_json, None)

    (issuer_2_gvt_cred_req, issuer_2_gvt_cred_req_metadata) = \
        await anoncreds.prover_create_credential_req(wallet_handle, prover_did, issuer_2_gvt_credential_offer_json,
                                                     issuer2_gvt_credential_def_json, master_secret_id)

    (issuer_2_gvt_cred, _, _) = \
        await anoncreds.issuer_create_credential(wallet_handle, issuer_2_gvt_credential_offer_json,
                                                 issuer_2_gvt_cred_req, gvt_2_cred_values_json, None, None)

    await anoncreds.prover_store_credential(wallet_handle, id_credential_3, issuer_2_gvt_cred_req_metadata,
                                            issuer_2_gvt_cred, issuer2_gvt_credential_def_json, None)

    await anoncreds.prover_store_credential(wallet_handle, id_credential_x, issuer_2_gvt_cred_req_metadata,
                                            issuer_2_gvt_cred, issuer2_gvt_credential_def_json, None)

    return issuer1_gvt_credential_def_json, issuer_1_gvt_credential_offer_json, issuer_1_gvt_cred_req, \
           issuer_1_gvt_cred_req_metadata, issuer_1_gvt_cred,
