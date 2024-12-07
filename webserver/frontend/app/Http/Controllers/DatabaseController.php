<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class DatabaseController extends Controller
{
    public function save(Request $request)
    {
        $data = $request->validate([
            'key' => 'required|string',
            'value' => 'required|string',
        ]);

        DB::table('key_values')->insert($data);

        return response()->json(['success' => true], 200);
    }

    public function get(Request $request)
    {
        $key = $request->query('key');

        $value = DB::table('key_values')->where('key', $key)->value('value');

        return response()->json(['key' => $key, 'value' => $value], 200);
    }
}
