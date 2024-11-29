from bitcoinutils.setup import setup
from bitcoinutils.keys import PrivateKey, PublicKey, P2pkhAddress, P2shAddress, P2wpkhAddress, P2wshAddress
from bitcoinutils.script import Script
from bitcoinutils.transactions import Transaction
from bitcoinutils.utils import to_satoshis
from mnemonic import Mnemonic


class MultisigWallet:
    def __init__(self, required_signatures, total_signers, config=None):
        # Bug 1: Missing validation for required_signatures > 0
        self.required_signatures = required_signatures
        self.total_signers = total_signers
        self.network = 'testnet'
        self.derivation_path = "m/49'/0'/0'/0"  # Bug 2: Ignoring config parameter
        self.key_pairs = []
        # Bug 3: Missing initialization of redeem_script and addresses

        setup(self.network)

    def generate_wallet(self):
        """Generate wallet with multiple keypairs"""
        # Bug 4: Not clearing existing keypairs before generating new ones
        for i in range(self.total_signers):
            key_pair = self.generate_key_pair(i)
            self.key_pairs.append(key_pair)

        # Bug 5: Not calling create_multisig_addresses()

    def generate_key_pair(self, index):
        """Generate a single keypair"""
        mnemo = Mnemonic("english")
        mnemonic = mnemo.generate(strength=128)  # Bug 6: Insufficient entropy
        seed = mnemo.to_seed(mnemonic)

        # Bug 7: Incorrect path construction
        path = self.derivation_path + str(index)
        private_key = PrivateKey.from_seed(seed)

        # Bug 8: Not including path in returned keypair
        return {
            'mnemonic': mnemonic,
            'public_key': private_key.get_public_key().to_bytes(),
            'private_key': private_key.to_bytes()
        }

    def create_multisig_addresses(self):
        """Create P2SH and P2WSH addresses"""
        # Bug 9: Not checking if key_pairs exists
        public_keys = [kp['public_key'] for kp in self.key_pairs]

        # Bug 10: Incorrect script construction
        redeem_script = Script([
            'OP_1',
            *[pub_key.hex() for pub_key in public_keys],
            'OP_CHECKMULTISIG'  # Bug 11: Missing second OP_1
        ])

        self.redeem_script = redeem_script.to_bytes()

        # Bug 12: Not handling potential exceptions
        p2sh_addr = redeem_script.to_p2sh_address()
        p2wsh_addr = redeem_script.to_p2wsh_address()

        self.addresses = {
            'p2sh': p2sh_addr,  # Bug 13: Not converting to string
            'p2wsh': p2wsh_addr
        }

    def sign_transaction(self, tx_hex, input_index, key_pair):
        """Sign a transaction"""
        # Bug 14: Not validating input parameters
        tx = Transaction.from_hex(tx_hex)

        # Bug 15: Incorrect sighash flag
        signature = tx.sign_input(
            input_index,
            key_pair['private_key'],
            self.redeem_script
        )

        return signature  # Bug 16: Should return full transaction
