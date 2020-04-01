// see 3bot_connect : example/src/services/CryptoService.js

// import ed2curve from 'ed2curve'
import { encodeBase64, decodeBase64, encodeUTF8 } from 'tweetnacl-util';
import sodium from 'libsodium-wrappers';
import { entropyToMnemonic, mnemonicToEntropy } from 'bip39';

export default {
    async validateSignature(message, signature, publicKey) {
        await sodium.ready;
        publicKey = decodeBase64(publicKey);
        signature = decodeBase64(signature);
        const result = sodium.crypto_sign_open(signature, publicKey);
        return result;
    },
    async validateSignedAttempt(signedAttempt, publicKey) {
        await sodium.ready;

        publicKey = decodeBase64(publicKey);
        signedAttempt = decodeBase64(signedAttempt);

        const signResult = sodium.crypto_sign_open(signedAttempt, publicKey);

        if (!signResult) {
            throw new Error('Invalid signature.');
        }

        return signResult;
    },
    async decrypt(message, nonce, privateKey, pubkey) {
        message = decodeBase64(message);
        await sodium.ready;
        privateKey = sodium.crypto_sign_ed25519_sk_to_curve25519(
            decodeBase64(privateKey)
        );
        pubkey = sodium.crypto_sign_ed25519_pk_to_curve25519(
            decodeBase64(pubkey)
        );
        nonce = decodeBase64(nonce);
        let decrypted = sodium.crypto_box_open_easy(
            message,
            nonce,
            pubkey,
            privateKey
        );
        decrypted = encodeUTF8(decrypted);
        return decrypted;
    },
    async encrypt(message, privateKey, pubkey) {
        message = new TextEncoder().encode(message);
        await sodium.ready;
        privateKey = sodium.crypto_sign_ed25519_sk_to_curve25519(
            decodeBase64(privateKey)
        );
        pubkey = sodium.crypto_sign_ed25519_pk_to_curve25519(
            decodeBase64(pubkey)
        );

        const nonce = sodium.randombytes_buf(
            sodium.crypto_secretbox_NONCEBYTES
        );
        const encrypted = sodium.crypto_box_easy(
            message,
            nonce,
            pubkey,
            privateKey
        );
        return {
            encrypted: encodeBase64(encrypted),
            nonce: encodeBase64(nonce),
        };
    },
    async generateKeys(phrase) {
        await sodium.ready;
        if (!phrase) {
            phrase = entropyToMnemonic(
                sodium.randombytes_buf(sodium.crypto_box_SEEDBYTES / 2)
            );
        }
        const ken = new TextEncoder().encode(mnemonicToEntropy(phrase));
        const keys = sodium.crypto_sign_seed_keypair(ken);
        return {
            phrase,
            privateKey: encodeBase64(keys.privateKey),
            publicKey: encodeBase64(keys.publicKey),
        };
    },
    getEdPkInCurve(pubkey) {
        return encodeBase64(
            sodium.crypto_sign_ed25519_pk_to_curve25519(decodeBase64(pubkey))
        );
    },
};
