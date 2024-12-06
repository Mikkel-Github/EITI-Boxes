<template>
    <div class="Row" style="margin-bottom: 1rem; background-color: #212121; gap: 0; border-bottom: 2px solid #e9b66f;">
        <div class="Column">
            <img src="../../../images/logo.png" style="max-width: 6rem; height: auto;" />
        </div>
        <div class="Column Flex">
            <div class="Column Flex">
            </div>
            <div class="Row" style="padding: 2rem; padding-bottom: 0.4rem; padding-top: 0.4rem; gap: 2rem; background-color: #212121;">
                <a class="Header-Btn" href="/transportation">Transportation Setup</a>
                <span class="vr" />
                <a class="Header-Btn" href="/browse-reports" >Reports</a>

                <div class="Row Flex" />

                <button class="Header-Btn">Log out</button>
            </div>
        </div>
    </div>
</template>

<style>
.Header-Btn {
    font-weight: bold;
    color: #e9b66f;
    transition: color 0.2s;
}
.Header-Btn:hover {
    color: #b58848;
}
</style>
